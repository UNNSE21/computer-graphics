from filters_opencv.filters.point_filters import WHITE_RGB
from filters_opencv.image import Image


def invert(image: Image):
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [x - y for x, y in zip(WHITE_RGB, image[i, j])]
