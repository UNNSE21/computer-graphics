from copy import deepcopy

from filters_opencv.filters.local_filters.mathematical_morphology.dilation import dilation
from filters_opencv.filters.local_filters.mathematical_morphology.utils.constants import DEFAULT_PATTERN
from filters_opencv.filters.local_filters.mathematical_morphology.utils.methods import subtract, try_convert_pattern
from filters_opencv.image import Image


def black_hat(binary_image: Image, pattern=DEFAULT_PATTERN, base_pixel: tuple[int, int] = None):
    pattern = try_convert_pattern(pattern)
    if base_pixel is None:
        base_pixel = (len(pattern) // 2, len(pattern[0]) // 2)
    elif len(base_pixel) != 2:
        return 'There should be two numbers in the base_pixel'

    copy_image = deepcopy(binary_image)
    dilation(binary_image, pattern, base_pixel)
    subtract(binary_image, copy_image)
