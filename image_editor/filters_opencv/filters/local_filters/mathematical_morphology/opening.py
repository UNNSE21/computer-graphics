from filters_opencv.filters.local_filters.mathematical_morphology.dilation import dilation
from filters_opencv.filters.local_filters.mathematical_morphology.erosion import erosion
from filters_opencv.filters.local_filters.mathematical_morphology.utils.constants import (
    DEFAULT_PATTERN,
)
from filters_opencv.image import Image


def opening(binary_image: Image, base_pixel: tuple[int, int] = None, pattern=DEFAULT_PATTERN):
    if base_pixel is None:
        base_pixel = (int(len(pattern) / 2), int(len(pattern[0]) / 2))

    erosion(binary_image, base_pixel, pattern)
    dilation(binary_image, base_pixel, pattern)
