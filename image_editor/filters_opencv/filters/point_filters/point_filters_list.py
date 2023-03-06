from typing import Final

from filters_opencv.filters import *
from filters_opencv.filters.filter import Filter

point_filters: Final = [
    Filter('mirror_horizontally', {'opening_path': str, 'saving_path': str}, 'Horizontal mirror image', horizontally),
    Filter('mirror_vertically', {'opening_path': str, 'saving_path': str}, 'Vertically mirror image', vertically),
    Filter(
        'relocate',
        {'opening_path': str, 'saving_path': str, 'offset_x': int, 'offset_y': int},
        'Transfer images by the certain number of pixels',
        relocate
    ),
    Filter(
        'rotation',
        {'opening_path': str, 'saving_path': str, 'center_x': int, 'center_y': int, 'angle_rotation': int},
        'Rotates images relative to the certain pixel by the certain angle',
        rotate
    ),
    Filter(
        'scale',
        {'opening_path': str, 'saving_path': str, 'coefficient': float},
        'Changes the size of the image',
        scale
    ),
    Filter(
        'change_brightness',
        {'opening_path': str, 'saving_path': str, 'delta': int},
        'Changes the brightness of the image by a certain number',
        change_brightness
    ),
    Filter(
        'glass_effect',
        {'opening_path': str, 'saving_path': str},
        'Applies the glass effect to the image',
        glass_effect
    ),
    Filter(
        'gray_scale',
        {'opening_path': str, 'saving_path': str, 'nargs_rgb_percentage_ratio=*': float},
        'Makes an image in grayscale with a certain percentage for each color',
        gray_scale
    ),
    Filter('invert', {'opening_path': str, 'saving_path': str}, 'Inverts the image', invert),
    Filter(
        'sepia',
        {'opening_path': str, 'saving_path': str, 'nargs_coefficient=?': int, 'nargs_rgb_percentage_ratio=*': float},
        'Applies a sepia effect with a certain coefficient and a certain percentage for each color to the image',
        sepia
    ),
    Filter(
        'waves',
        {'opening_path': str, 'saving_path': str, 'direction': Direction},
        'Applies the effect of waves in a certain direction (vertical, horizontal) to the image',
        waves
    ),
]