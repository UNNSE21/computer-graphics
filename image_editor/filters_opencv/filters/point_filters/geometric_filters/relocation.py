from copy import deepcopy

from filters_opencv.filters.point_filters.utils.constants import BLACK_RGB
from filters_opencv.image import Image


def relocate(image: Image, offset_x: int, offset_y: int):
    offset_x = int(offset_x)
    offset_y = int(offset_y)
    copy_image = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            if (0 <= i - offset_y < image.height) and (0 <= j - offset_x < image.width):
                image[i, j] = copy_image[i - offset_y, j - offset_x]
            else:
                image[i, j] = BLACK_RGB
