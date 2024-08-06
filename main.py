from api import get_feed, parse_feed


def main():
    print(parse_feed(get_feed()))


if __name__ == "__main__":
    main()
