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
        for argument, type_argument in command.arguments.items():
            if 'nargs' in argument:
                parser_command.add_argument(
                    argument[6:argument.find('=')],
                    type=type_argument,
                    nargs=argument[-1],
                )
            else:
                parser_command.add_argument(argument, type=type_argument)
        parser_command.set_defaults(func=command.func)

    return parser.parse_args()

