from datetime import datetime, timedelta, timezone

import requests
from tabulate import tabulate

from deal.config import CONFIG, POST_HEADERS, REQUEST_BODY


def get_feed():
    session = requests.Session()
    all_results = []
    page = 1
    try:
        initial_response = session.post(
            CONFIG["post_url"], headers=POST_HEADERS, json=REQUEST_BODY, timeout=10
        )
        initial_response.raise_for_status()
        cookies = initial_response.cookies.get_dict()
        session.cookies.update(cookies)

        while True:
            REQUEST_BODY["page"] = page
            response = session.post(
                CONFIG["post_url"], headers=POST_HEADERS, json=REQUEST_BODY, timeout=10
            )
            response.raise_for_status()
            data = response.json()
            asset_search_results = data.get("assetSearchResults", [])
            if asset_search_results is None or len(asset_search_results) == 0:
                break
            all_results.append(data)
            page += 1
    except requests.exceptions.Timeout:
        print("The request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    return all_results


def parse_feed(feed):
    for page_data in feed:
        asset_search_results = page_data.get("assetSearchResults", [])
        for asset in asset_search_results:
           print(asset.get("assetShortDescription"), f"https://www.govdeals.com/asset/{asset.get("assetId")}/{asset.get("accountId")}")


def list_ending_feed(feed):
    current_time = datetime.now(timezone.utc)
    current_date = current_time.date()

    table_data = []
    headers = ["Description", "URL", "Current Bid"]

    for page_data in feed:
        asset_search_results = page_data.get("assetSearchResults", [])
        for asset in asset_search_results:
            asset_end_date_str = asset.get("assetAuctionEndDate")
            if asset_end_date_str:
                asset_end_date = datetime.fromisoformat(asset_end_date_str).astimezone(
                    timezone.utc
                )
                if (
                    asset_end_date.date() == current_date  or asset_end_date.date() == current_date + timedelta(days=1)
                    and asset_end_date > current_time
                ):
                    description = asset.get("assetShortDescription")
                    url = f"https://www.govdeals.com/asset/{asset.get('assetId')}/{asset.get('accountId')}"
                    current_bid = asset.get("currentBid")
                    table_data.append([description, url, current_bid])
    print(tabulate(table_data, headers=headers, tablefmt="pretty"))
