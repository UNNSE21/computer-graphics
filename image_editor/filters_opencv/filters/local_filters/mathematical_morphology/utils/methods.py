from filters_opencv.filters.point_filters.utils.constants import BLACK_RGB, WHITE_RGB
from filters_opencv.image import Image


def subtract(reduced_image: Image, deductible_image: Image):
    for i in range(reduced_image.height):
        for j in range(reduced_image.width):
            if deductible_image[i, j] == BLACK_RGB:
                reduced_image[i, j] = WHITE_RGB


def try_convert_pattern(pattern):
    if isinstance(pattern, str):
        image = Image(pattern)
        return image.get_bitmap()
    if isinstance(pattern, Image):
        return pattern.get_bitmap()
    return pattern
