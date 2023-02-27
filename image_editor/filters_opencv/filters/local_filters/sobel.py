from math import sqrt

from numpy import array

from filters_opencv.filters.local_filters.utils.constants import SOBEL_KERNEL_X, SOBEL_KERNEL_Y
from filters_opencv.image import Image


def sobel(image: Image):
    bitmap_x = _sobel(image, SOBEL_KERNEL_X)
    bitmap_y = _sobel(image, SOBEL_KERNEL_Y)

    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [sqrt(x ** 2 + y ** 2) for x, y in zip(bitmap_x[j][i], bitmap_y[j][i])]


def _sobel(image: Image, kernel):
    horizontal_kernel = kernel[0]
    vertical_kernel = array(kernel)[:, 0]

    bitmap = []
    for i in range(image.height):
        line = []
        for j in range(image.width):
            pixel = (0, 0, 0)
            radius = int(len(horizontal_kernel) / 2)
            for k in range(-radius, radius + 1):
                index = min(max(0, k + j), image.width - 1)
                pixel = [x + y * horizontal_kernel[k + radius] for x, y in zip(pixel, image[i, index])]
            line.append(tuple(reversed(pixel)))
        bitmap.append(line)

    new_bitmap = []
    for i in range(image.width):
        line = []
        for j in range(image.height):
            pixel = (0, 0, 0)
            radius = int(len(horizontal_kernel) / 2)
            for k in range(-radius, radius + 1):
                index = min(max(0, k + j), image.height - 1)
                pixel = [x + y * vertical_kernel[k + radius] for x, y in zip(pixel, bitmap[index][i])]
            line.append(tuple(reversed(pixel)))
        new_bitmap.append(line)
    return new_bitmap
