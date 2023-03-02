from copy import deepcopy
from math import sqrt

from numpy import array

from filters_opencv.filters.local_filters.utils.enums import Direction
from filters_opencv.image import Image


def apply_kernels(image: Image, kernels):
    copy_image_1 = deepcopy(image)
    copy_image_2 = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            match len(kernels):
                case 1:
                    image[i, j] = _calculate_pixel_color(copy_image_1, j, i, kernels[0])
                case 2:
                    pixel_x = _calculate_pixel_color(copy_image_1, j, i, kernels[0])
                    pixel_y = _calculate_pixel_color(copy_image_2, j, i, kernels[1])
                    image[i, j] = [sqrt(x ** 2 + y ** 2) for x, y in zip(pixel_x, pixel_y)]


def _calculate_pixel_color(image: Image, pos_x: int, pos_y: int, kernel):
    pixel = (0, 0, 0)
    radius_x, radius_y = int(len(kernel) / 2), int(len(kernel[0]) / 2)
    kernel_i, kernel_j = 0, 0
    for i in range(pos_y - radius_y, pos_y + radius_y + 1):
        temp_i = min(max(0, i), image.height - 1)
        kernel_j = 0
        for j in range(pos_x - radius_x, pos_x + radius_x + 1):
            temp_j = min(max(0, j), image.width - 1)
            pixel = [x + y * kernel[kernel_i][kernel_j] for x, y in zip(pixel, image[temp_i, temp_j])]
            kernel_j += 1
        kernel_i += 1

    return pixel


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
