from copy import deepcopy

from filters_opencv.filters.local_filters.mathematical_morphology.utils.constants import (
    DEFAULT_PATTERN,
    BLACK_RGB,
    WHITE_RGB,
)
from filters_opencv.filters.local_filters.mathematical_morphology.utils.methods import try_convert_pattern
from filters_opencv.image import Image


def erosion(binary_image: Image, pattern=DEFAULT_PATTERN, base_pixel: tuple[int, int] = None):
    pattern = try_convert_pattern(pattern)
    if base_pixel is None:
        base_pixel = (len(pattern) // 2, len(pattern[0]) // 2)
    elif len(base_pixel) != 2:
        return 'There should be two numbers in the base_pixel'
    copy_image = deepcopy(binary_image)
    for i in range(binary_image.height):
        for j in range(binary_image.width):
            binary_image[i, j] = _calculate_pixel_color(copy_image, base_pixel, pattern, j, i)


def _calculate_pixel_color(image: Image, base_pixel: tuple[int, int], pattern, pos_x: int, pos_y: int):
    index_i = 0
    for i in range(pos_y - base_pixel[0], pos_y - base_pixel[0] + len(pattern)):
        index_j = 0
        for j in range(pos_x - base_pixel[1], pos_x - base_pixel[1] + len(pattern[0])):
            if not(0 <= i < image.height and 0 <= j < image.width) and pattern[index_i][index_j] == BLACK_RGB:
                return WHITE_RGB
            if image[i, j] != pattern[index_i][index_j] and pattern[index_i][index_j] == BLACK_RGB:
                return WHITE_RGB
            index_j += 1
        index_i += 1
    return BLACK_RGB
