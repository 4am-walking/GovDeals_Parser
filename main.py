from api import get_feed, parse_feed
from config import args

def main():
    if args.list_all:
        print(parse_feed(get_feed()))


if __name__ == "__main__":
    main()
