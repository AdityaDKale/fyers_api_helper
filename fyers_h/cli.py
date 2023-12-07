import argparse
from .config import set_config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("arg1", help="[config]")

    args = parser.parse_args()
    if args.arg1 == "config":
        set_config()


if __name__ == "__main__":
    main()
