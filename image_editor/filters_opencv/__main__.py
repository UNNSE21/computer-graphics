from loguru import logger
from filters_opencv.filters import *
from filters_opencv.image import Image
from filters_opencv.filters.global_filters.embossing import embossing

def main():
    """Main method. Entry point."""
    image = Image("images/2.png")
    embossing(image)
    try:
        
        image.show()
    except Exception as ex:
        logger.critical('You have done something wrong! {0}'.format(str(ex)))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.critical('Shutting down, bye!')
