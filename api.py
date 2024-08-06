import json

import requests

from config import CONFIG, POST_HEADERS, REQUEST_BODY


def get_feed():
    session = requests.Session()
    try:
        initial_response = session.post(
            CONFIG["post_url"], headers=POST_HEADERS, json=REQUEST_BODY, timeout=10
        )
        initial_response.raise_for_status()
        cookies = initial_response.cookies.get_dict()
        session.cookies.update(cookies)
        response = session.post(
            CONFIG["post_url"], headers=POST_HEADERS, json=REQUEST_BODY, timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The request timed out")
        return None


def parse_feed(feed):
    for asset in feed["assetSearchResults"]:
        print(asset.get("assetShortDescription"))


print(parse_feed(get_feed()))
