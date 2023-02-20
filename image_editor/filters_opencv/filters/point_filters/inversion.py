from filters_opencv.image import Image
from typing import Final


WHITE_RGB: Final = (255, 255, 255)


def invert(image: Image):
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [x - y for x, y in zip(WHITE_RGB, image[i, j])]
