from copy import deepcopy

from filters_opencv.filters.local_filters.utils.methods.calculation_kernel import calculate_kernel_motion_blur
from filters_opencv.image import Image


def motion_blur(image: Image, size: int):
    copy_image = deepcopy(image)
    kernel = calculate_kernel_motion_blur(size)
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = _calculate_pixel_color(copy_image, j, i, kernel)


def _calculate_pixel_color(image: Image, pos_x: int, pos_y: int, kernel):
    pixel = (0, 0, 0)
    radius = int(len(kernel) / 2)
    kernel_i = 0
    for i in range(pos_y - radius, pos_y + radius + 1):
        temp_i = min(max(0, i), image.height - 1)
        temp_j = min(max(0, temp_i + (pos_x - pos_y)), image.width - 1)
        pixel = [x + y * kernel[kernel_i] for x, y in zip(pixel, image[temp_i, temp_j])]
        kernel_i += 1
    return pixel
