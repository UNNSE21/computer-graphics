from filters_opencv.filters.local_filters.blur.arithmetic_mean.utils import arithmetic_mean
from filters_opencv.image import Image


def not_optimized_blur(image: Image, radius_x: int, radius_y: int):
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = arithmetic_mean(image, j, i, radius_x, radius_y)
