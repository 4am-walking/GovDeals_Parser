import argparse

parser = argparse.ArgumentParser(
    prog="GovDeals Parser",
    description="This program parses GovDeals and displays info about products",
)
parser.add_argument("--list-all", action="store_true", help="Fetch and list all assets")
parser.add_argument(
    "--end-soon", action="store_true", help="Fetch and list assets ending soon"
)
parser.add_argument("-z", "--zipcode", type=str, help="Set the zipcode for the search")
parser.add_argument(
    "-m",
    "--miles",
    type=int,
    help="Set the search radius in miles. Options are 25, 50, 75, 100, 250",
)
args = parser.parse_args()

CONFIG = {
    "get_url": f"https://www.govdeals.com/computers-parts-supplies/filters?zipcode={args.zipcode}&miles={args.miles}&pn=1&ps=120",
    "post_url": "https://maestro.lqdt1.com/search/list",
    "get_url_page_2": f"https://www.govdeals.com/computers-parts-supplies/filters?zipcode={args.zipcode}&miles={args.miles}&pn=2&ps=120&so=&sf=bestfit",
}
GET_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "DNT": "1",
    "Sec-GPC": "1",
    "Priority": "u=0, i",
}
POST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "x-api-key": "af93060f-337e-428c-87b8-c74b5837d6cd",
    "x-api-correlation-id": "39197d22-bf35-465d-b778-0761c7f2d7c9",
    "x-ecom-session-id": "c5927321-d817-4cf1-a6d7-fc076cbe0f6d",
    "x-referer": f"https://www.govdeals.com/computers-parts-supplies/filters?zipcode={args.zipcode}&miles={args.miles}&pn=1&ps=120",
    "x-user-id": "-1",
    "x-page-unique-id": "aHR0cHM6Ly93d3cuZ292ZGVhbHMuY29tL2NvbXB1dGVycy1wYXJ0cy1zdXBwbGllcw=",
    "Ocp-Apim-Subscription-Key": "cf620d1d8f904b5797507dc5fd1fdb80",
    "x-user-timezone": "America/New_York",
    "Content-Type": "application/json",
    "Origin": "https://www.govdeals.com",
    "Connection": "keep-alive",
    "Referer": "https://www.govdeals.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "DNT": "1",
    "Sec-GPC": "1",
}
REQUEST_BODY = {
    "categoryIds": "",
    "businessId": "GD",
    "searchText": "*",
    "isQAL": False,
    "locationId": None,
    "model": "",
    "makebrand": "",
    "auctionTypeId": None,
    "page": 1,
    "displayRows": 120,
    "sortField": "bestfit",
    "sortOrder": "desc",
    "sessionId": "bd8fc3a9-9f2c-479d-992d-f4e7356894ee",
    "requestType": "search",
    "responseStyle": "productsOnly",
    "facets": [
        "categoryName",
        "auctionTypeID",
        "condition",
        "saleEventName",
        "sellerDisplayName",
        "product_pricecents",
        "isReserveMet",
        "hasBuyNowPrice",
        "isReserveNotMet",
        "sellerType",
        "warehouseId",
        "region",
        "currencyTypeCode",
        "countryDesc",
        "tierId",
    ],
    "facetsFilter": [
        '{!tag=product_category_external_id}product_category_external_id:"t2"',
        '{!tag=product_category_external_id}product_category_external_id:"29"',
    ],
    "timeType": "",
    "sellerTypeId": None,
    "accountIds": [],
    "zipcode": f"{args.zipcode}",
    "proximityWithinDistance": f"{args.miles}",
}
