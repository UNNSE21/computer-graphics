from loguru import logger

from filters_opencv.cmd_input import cmd_input


def main():
    """Main method. Entry point."""
    try:
        cmd_input()
    except Exception as ex:
        logger.critical('You have done something wrong! {0}'.format(str(ex)))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.critical('Shutting down, bye!')
