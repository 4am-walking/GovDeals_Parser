from api import get_feed, list_ending_feed, parse_feed
from config import args


def main():
    if args.miles not in (25, 50, 75, 100, 250) or not args.zipcode:
        print(
            "Please provide a zipcode and relevant miles. Miles must be one of 25, 50, 75, 100, 250"
        )
        return
    if args.list_all:
        print(parse_feed(get_feed()))
    elif args.end_soon:
        print(list_ending_feed(get_feed()))


if __name__ == "__main__":
    main()
