from copy import deepcopy
from random import random

from filters_opencv.image import Image


def glass_effect(image: Image):
    copy_image = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            x, y = _calculate_index(i), _calculate_index(j)
            if 0 <= x < image.height and 0 <= y < image.width:
                image[i, j] = copy_image[x, y]


def _calculate_index(index: int) -> int:
    return int(index + (random() - 0.5) * 10)
