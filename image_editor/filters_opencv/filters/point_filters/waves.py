from copy import deepcopy
from math import sin, pi

from filters_opencv.filters.point_filters.utils.enums import Direction
from filters_opencv.image import Image


def waves(image: Image, direction: Direction):
    match direction:
        case Direction.vertical:
            _waves(image, _calculate_index_vertical)
        case Direction.horizontal:
            _waves(image, _calculate_index_horizontal)


def _waves(image: Image, calculator_index):
    copy_image = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            x, y = calculator_index(i, j)
            temp_x = max(min(x, image.height - 1), 0)
            temp_y = max(min(y, image.width - 1), 0)
            image[i, j] = copy_image[temp_x, temp_y]


def _calculate_index_vertical(i: int, j: int):
    return int(i + 20 * sin(2 * pi * i / 30)), j


def _calculate_index_horizontal(i: int, j: int):
    return int(i + 20 * sin(2 * pi * j / 60)), j