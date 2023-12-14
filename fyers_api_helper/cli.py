import argparse
from .config import set_config, set_config_manually, print_config
from .access import run, print_access, set_access_manually, check_valid, load_access
from .search import search


def main():
    '''
    Command Line Interface for Fyers API Helper
    '''

    parser = argparse.ArgumentParser(
        description='CLI for configuration and access operations.'
    )

    subparsers = parser.add_subparsers(
        title='subcommands',
        dest='command',
        help='Choose a command'
    )

    # Config subcommand
    config_parser = subparsers.add_parser('config', help='Open the config')
    config_parser.set_defaults(func=set_config)
    config_parser.add_argument(
        '-p',
        '--print',
        action='store_true',
        dest='print_config',
        help='Print the config'
    )
    config_parser.add_argument(
        '-s',
        '--set',
        nargs=2,
        metavar=('KEY', 'VALUE'),
        dest='set_config',
        help='Set config manually'
    )

    # Access subcommand
    access_parser = subparsers.add_parser(
        'access',
        help='Open the access'
    )
    access_parser.set_defaults(func=run)
    access_parser.add_argument(
        '-v',
        '--is-valid',
        action='store_true',
        dest='is_valid',
        help='Check if the access token is valid'
    )
    access_parser.add_argument(
        '-p',
        '--print',
        action='store_true',
        dest='print_access',
        help='Print the access token'
    )
    access_parser.add_argument(
        '-s',
        '--set',
        nargs=2,
        metavar=('TOKEN', 'AUTODATE'),
        dest='set_access',
        help='Set access token manually'
    )

    # Search subcommand
    search_parser = subparsers.add_parser('search',
                                          help='Search Symbols')
    search_parser.set_defaults(func=search)
    search_parser.add_argument(
        'search_query',
        type=lambda x: int(x) if x is not None else None,
        nargs='?',
        help='Maximum number of matches (default=10)'
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
    elif args.command == 'config':
        if args.print_config:
            print_config()
        elif args.set_config:
            set_config_manually(args.set_config[0], args.set_config[1])
        elif args.func:
            args.func()
    elif args.command == 'access':
        if args.is_valid:
            try:
                data = load_access()
                check_valid(data, silent=False)
            except Exception:
                print("Invalid Access Token. Please Generate Token Again")
                exit(1)
        elif args.print_access:
            print_access()
        elif args.set_access:
            set_access_manually(args.set_access[0], args.set_access[1])
        elif args.func:
            args.func()
    elif args.command == 'search':
        if args.search_query:
            args.func(args.search_query)
        else:
            args.func()


if __name__ == "__main__":
    main()
