import argparse
from .config import set_config, set_config_manually, print_config


def function4():
    pass


def main():
    parser = argparse.ArgumentParser(
        description='CLI for configuration and access operations.')

    subparsers = parser.add_subparsers(
            title='subcommands',
            dest='command',
            help='Choose a command')

    # Config subcommand
    config_parser = subparsers.add_parser('config', help='Open the config')
    config_parser.set_defaults(func=set_config)
    config_parser.add_argument(
            '-p',
            '--print',
            action='store_true',
            dest='print_config',
            help='Print the config')
    config_parser.add_argument(
            '-s',
            '--set',
            nargs=2,
            metavar=('KEY', 'VALUE'),
            dest='set_config',
            help='Set config manually')

    # Access subcommand
    access_parser = subparsers.add_parser(
            'access',
            help='Open the access')
    access_parser.set_defaults(func=function4)
    access_parser.add_argument(
            '-v',
            '--is-valid',
            action='store_true',
            dest='is_valid',
            help='Check if the access token is valid')
    access_parser.add_argument(
            '-p',
            '--print',
            action='store_true',
            dest='print_access',
            help='Print the access token')
    access_parser.add_argument('-s',
                               '--set',
                               nargs=2,
                               metavar=(
                                   'TOKEN',
                                   'AUTODATE'),
                               dest='set_access',
                               help='Set access token manually')

    args = parser.parse_args()

    if args.command == 'config':
        if args.print_config:
            print_config()
        elif args.set_config:
            set_config_manually(args.set_config[0], args.set_config[1])
        elif args.func:
            args.func()
    elif args.command == 'access':
        if args.is_valid:
            pass  # Add logic for function4
        elif args.print_access:
            pass  # Add logic for function4
        elif args.set_access:
            pass  # Add logic for function7


if __name__ == "__main__":
    main()
