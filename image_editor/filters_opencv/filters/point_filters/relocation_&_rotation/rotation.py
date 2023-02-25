from copy import deepcopy
from math import cos, sin

from filters_opencv.filters.point_filters.utils.constants import BLACK_RGB
from filters_opencv.image import Image


def rotate(image: Image, center_x: int, center_y: int, angle_rotation: float):
    copy_image = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            new_x = int((j - center_x) * cos(angle_rotation) - (i - center_y) * sin(angle_rotation) + center_x)
            new_y = int((j - center_x) * sin(angle_rotation) + (i - center_y) * cos(angle_rotation) + center_y)
            if (0 <= new_x < image.width) and (0 <= new_y < image.height):
                image[i, j] = copy_image[new_y, new_x]
            else:
                image[i, j] = BLACK_RGB
