import argparse

from loguru import logger

from filters_opencv.image import Image


def apply_command(args):
    logger.info('The command begins its execution')
    image = Image(args.opening_path)
    args_list = list(vars(args).values())
    correct_argument = []
    for argument in args_list[2:-1]:
        if argument is not None and argument != []:
            correct_argument.append(argument)
    msg_error = args.func(image, *correct_argument)
    if msg_error is not None:
        raise argparse.ArgumentTypeError(msg_error)
    image.save(args.saving_path)
    logger.info('The command has completed its execution')
