import json

import requests

from config import CONFIG, POST_HEADERS, REQUEST_BODY


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
            asset_search_results = data.get('assetSearchResults', [])
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
            print(asset.get("assetShortDescription"))
