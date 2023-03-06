from loguru import logger

from filters_opencv.image import Image


def apply_command(args):
    logger.info('The command begins its execution')
    image = Image(args.opening_path)
    args_list = list(vars(args).values())
    args.func(image, *map(float, args_list[2:-1]))
    image.save(args.saving_path)
    logger.info('The command has completed its execution')
