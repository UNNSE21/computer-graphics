from copy import deepcopy
from math import ceil

from filters_opencv.filters.local_filters.blur.utils.calculation_kernel import calculate_kernel_gaussian_blur
from filters_opencv.image import Image


def blur_gaussian(image: Image, sigma: float, size: int = None):
    denominator = 2 * sigma * sigma
    if size is None:
        size = ceil(3 * sigma)
    kernel = calculate_kernel_gaussian_blur(size, denominator)

    _blur_horizontal(image, size, kernel)
    _blur_vertically(image, size, kernel)


def _blur_horizontal(image: Image, size: int, kernel):
    copy_image = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            sum_coefficients = 0
            pixel = (0, 0, 0)
            for k in range(-size, size + 1):
                index = k + j
                if 0 <= index < image.width:
                    pixel = [x + y * kernel[k] for x, y in zip(pixel, copy_image[i, index])]
                    sum_coefficients += kernel[k]
            pixel = [x / sum_coefficients for x in pixel]
            image[i, j] = pixel


def _blur_vertically(image: Image, size: int, kernel):
    copy_image = deepcopy(image)
    for i in range(image.width):
        for j in range(image.height):
            sum_coefficients = 0
            pixel = [0, 0, 0]
            for k in range(-size, size + 1):
                index = k + j
                if 0 <= index < image.height:
                    pixel = [x + y * kernel[k] for x, y in zip(pixel, copy_image[index, i])]
                    sum_coefficients += kernel[k]
            pixel = [x / sum_coefficients for x in pixel]
            image[j, i] = pixel
