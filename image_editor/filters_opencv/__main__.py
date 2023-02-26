from loguru import logger
from filters_opencv.filters import *
from filters_opencv.image import Image


def main():
    """Main method. Entry point."""
    try:
<<<<<<< HEAD
        image = Image("images/4.png")
        waves(image)
=======
        image = Image("images/1.png")
>>>>>>> 0094702ad6695821baef782e00eb44923964dbfe
        image.show()
    except Exception as ex:
        logger.critical('You have done something wrong! {0}'.format(str(ex)))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.critical('Shutting down, bye!')
