from copy import deepcopy

from filters_opencv.filters.local_filters.mathematical_morphology.dilation import dilation
from filters_opencv.filters.local_filters.mathematical_morphology.erosion import erosion
from filters_opencv.filters.local_filters.mathematical_morphology.utils.constants import DEFAULT_PATTERN
from filters_opencv.filters.local_filters.mathematical_morphology.utils.methods import subtract
from filters_opencv.image import Image


def grad(binary_image: Image, base_pixel: tuple[int, int] = None, pattern=DEFAULT_PATTERN):
    if base_pixel is None:
        base_pixel = (len(pattern) // 2, len(pattern[0]) // 2)
    copy_image = deepcopy(binary_image)
    dilation(binary_image, base_pixel, pattern)
    erosion(copy_image, base_pixel, pattern)
    subtract(binary_image, copy_image)
