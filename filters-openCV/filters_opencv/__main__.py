from loguru import logger

import filters_opencv.filters.point_filters.mirror_image as mirror_image
from filters_opencv.filters.local_filters.arithmetic_mean import arithmetic_mean
from filters_opencv.filters.global_filters.median_filters import (
    averaging_color,
    darkening,
    lightening,
)
from filters_opencv.filters.point_filters.inversion import invert
from filters_opencv.filters.point_filters.scale import scale
from filters_opencv.image import Image


def main():
    """Main method. Entry point."""
    try:
        image = Image("images/2.png")

        image.show()
    except Exception as ex:
        logger.critical('You have done something wrong! {0}'.format(str(ex)))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.critical('Shutting down, bye!')
