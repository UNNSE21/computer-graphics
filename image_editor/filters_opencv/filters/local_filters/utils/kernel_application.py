from copy import deepcopy
from math import sqrt

from filters_opencv.image import Image


def apply_kernels(image: Image, kernels):
    copy_image_1 = deepcopy(image)
    copy_image_2 = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            match len(kernels):
                case 1:
                    image[i, j] = calculate_pixel_color(copy_image_1, j, i, kernels[0])
                case 2:
                    pixel_x = calculate_pixel_color(copy_image_1, j, i, kernels[0])
                    pixel_y = calculate_pixel_color(copy_image_2, j, i, kernels[1])
                    image[i, j] = [sqrt(x ** 2 + y ** 2) for x, y in zip(pixel_x, pixel_y)]


def calculate_pixel_color(image: Image, pos_x: int, pos_y: int, kernel):
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
