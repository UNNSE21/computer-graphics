import argparse

from filters_opencv.command import apply_command
from filters_opencv.filters.filter_list import filters


def cmd_input():
    """Input method."""
    args = _parse_args()
    apply_command(args)


def _parse_args():
    parser = argparse.ArgumentParser(description='Applying filters')
    subparsers = parser.add_subparsers()
    for command in filters:
        parser_command = subparsers.add_parser(command.name, help=command.help)
        for argument in command.arguments:
            parser_command.add_argument(argument)
        parser_command.set_defaults(func=command.func)

    return parser.parse_args()
