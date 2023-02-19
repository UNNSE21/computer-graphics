from loguru import logger

import filters_opencv.filters.mirror_image as mirror_image
from filters_opencv.filters.arithmetic_mean import arithmetic_mean
from filters_opencv.filters.changing_histogram import (
    average_color,
    darken,
    lighten,
)
from filters_opencv.filters.inversion import invert
from filters_opencv.filters.scale import scale
from filters_opencv.image import Image


def main():
    """Main method. Entry point."""
    try:
        image = Image("../images/2.png")

        image.show()
    except Exception as ex:
        logger.critical('You have done something wrong! {0}'.format(str(ex)))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.critical('Shutting down, bye!')
