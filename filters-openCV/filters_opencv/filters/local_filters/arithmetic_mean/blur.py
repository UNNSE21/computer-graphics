from filters_opencv.filters.local_filters.arithmetic_mean import _arithmetic_mean
from filters_opencv.image import Image


def blur(image: Image, radius_x: int, radius_y: int):
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = _arithmetic_mean(image, j, i, radius_x, radius_y)
