from filters_opencv.filters.local_filters.mathematical_morphology.dilation import dilation
from filters_opencv.filters.local_filters.mathematical_morphology.erosion import erosion
from filters_opencv.filters.local_filters.mathematical_morphology.utils.constants import DEFAULT_PATTERN
from filters_opencv.filters.local_filters.mathematical_morphology.utils.methods import try_convert_pattern
from filters_opencv.image import Image


def closing(binary_image: Image, pattern=DEFAULT_PATTERN, base_pixel: tuple[int, int] = None):
    pattern = try_convert_pattern(pattern)
    if base_pixel is None:
        base_pixel = (len(pattern) // 2, len(pattern[0]) // 2)
    elif len(base_pixel) != 2:
        return 'There should be two numbers in the base_pixel'

    dilation(binary_image, pattern, base_pixel)
    erosion(binary_image, pattern, base_pixel)
