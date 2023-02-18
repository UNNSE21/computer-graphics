from loguru import logger

from filters_opencv.filters.inversion import invert
from filters_opencv.filters.scale import scale
from filters_opencv.image import Image

import filters_opencv.filters.mirror_image as mirror_image


def main():
    """Main method. Entry point."""
    try:
        image = Image("../images/2.png")
        # invert(image)
        # mirror_image.vertically(image)
        # mirror_image.horizontally(image)
        # scale(image, 0.5)

        image.show()
    except Exception as ex:
        logger.critical('You have done something wrong! {0}'.format(str(ex)))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.critical('Shutting down, bye!')
