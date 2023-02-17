from loguru import logger

from filters_opencv.filters.inversion import inversion
from filters_opencv.image import Image

import filters_opencv.filters.mirror_image as mirror_image


def main():
    """Main method. Entry point."""
    try:
        image = Image("../images/1.png")
        inversion(image)
        mirror_image.vertically(image)
        mirror_image.horizontally(image)
        image.show()
    except Exception as ex:
        logger.critical('You have done something wrong! {0}'.format(str(ex)))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.critical('Shutting down, bye!')
