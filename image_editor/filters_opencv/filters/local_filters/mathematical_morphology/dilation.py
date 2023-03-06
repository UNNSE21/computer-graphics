from copy import deepcopy

from filters_opencv.filters.local_filters.mathematical_morphology.utils.constants import (
    DEFAULT_PATTERN,
    BLACK_RGB,
)
from filters_opencv.filters.local_filters.mathematical_morphology.utils.methods import try_convert_pattern
from filters_opencv.image import Image


def dilation(binary_image: Image, pattern=DEFAULT_PATTERN, base_pixel: tuple[int, int] = None):
    pattern = try_convert_pattern(pattern)
    if base_pixel is None:
        base_pixel = (len(pattern) // 2, len(pattern[0]) // 2)
    elif len(base_pixel) != 2:
        return 'There should be two numbers in the base_pixel'

    copy_image = deepcopy(binary_image)
    for i in range(binary_image.height):
        for j in range(binary_image.width):
            _change_pixels_color(binary_image, copy_image, base_pixel, pattern, j, i)


def _change_pixels_color(image: Image, copy_image: Image, base_pixel: tuple[int, int], pattern, pos_x: int, pos_y: int):
    if copy_image[pos_y, pos_x] == pattern[base_pixel[0]][base_pixel[1]]:
        index_i = 0
        for i in range(pos_y - base_pixel[0], pos_y - base_pixel[0] + len(pattern)):
            temp_i = max(min(i, image.height - 1), 0)
            index_j = 0
            for j in range(pos_x - base_pixel[1], pos_x - base_pixel[1] + len(pattern[0])):
                temp_j = max(min(j, image.width - 1), 0)
                if pattern[index_i][index_j] == BLACK_RGB:
                    image[temp_i, temp_j] = BLACK_RGB
                index_j += 1
            index_i += 1
