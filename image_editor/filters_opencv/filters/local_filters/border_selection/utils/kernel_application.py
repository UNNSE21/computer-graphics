from math import sqrt

from numpy import array

from filters_opencv.filters.local_filters.border_selection.utils.enums import Direction
from filters_opencv.image import Image


def apply_split_kernels(image: Image, kernels):
    match len(kernels):
        case 1:
            bitmap = _calculate_bitmap(image.get_bitmap(), kernels[0])
            for i in range(image.height):
                for j in range(image.width):
                    image[i, j] = bitmap[j][i]

        case 2:
            bitmap_x = _calculate_bitmap(image.get_bitmap(), kernels[0])
            bitmap_y = _calculate_bitmap(image.get_bitmap(), kernels[1])

            for i in range(image.height):
                for j in range(image.width):
                    image[i, j] = [sqrt(x ** 2 + y ** 2) for x, y in zip(bitmap_x[j][i], bitmap_y[j][i])]


def _calculate_bitmap(bitmap, kernel):
    horizontal_kernel = kernel[0]
    vertical_kernel = array(kernel)[:, 0]
    height, width = len(bitmap), len(bitmap[0])

    bitmap = _calculate_bitmap_in_one_direction(bitmap, horizontal_kernel, height, width, Direction.horizontal)
    bitmap = _calculate_bitmap_in_one_direction(bitmap, vertical_kernel, width, height, Direction.vertical)

    return bitmap


def _calculate_bitmap_in_one_direction(bitmap, kernel, max_i: int, max_j: int, direction: Direction):
    temp_bitmap = []
    for i in range(max_i):
        line = []
        for j in range(max_j):
            pixel = (0, 0, 0)
            radius = int(len(kernel) / 2)
            for k in range(-radius, radius + 1):
                index = min(max(0, k + j), max_j - 1)
                match direction:
                    case Direction.horizontal:
                        pixel = [x + y * kernel[k + radius] for x, y in zip(pixel, bitmap[i][index])]
                    case Direction.vertical:
                        pixel = [x + y * kernel[k + radius] for x, y in zip(pixel, bitmap[index][i])]
            line.append(pixel)
        temp_bitmap.append(line)
    return temp_bitmap
