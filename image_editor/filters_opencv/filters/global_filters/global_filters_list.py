from typing import Final

from filters_opencv.filters import *
from filters_opencv.filters.filter import Filter

global_filters: Final = [
    Filter(
        'average_color',
        {'opening_path': str, 'saving_path': str, 'nargs_coefficient=?': float},
        'Averages the color of the image',
        average_color
    ),
    Filter(
        'darken',
        {'opening_path': str, 'saving_path': str, 'nargs_coefficient=?': float},
        'Darkens the image',
        darken
    ),
    Filter(
        'gray_world',
        {'opening_path': str, 'saving_path': str},
        'Gray World',
        gray_world
    ),
    Filter(
        'lighten',
        {'opening_path': str, 'saving_path': str, 'nargs_coefficient=?': float},
        'Brightens the image',
        lighten
    ),
    Filter(
        'autolevels',
        {'opening_path': str, 'saving_path': str},
        'Image correction',
        autolevels
    ),
    Filter(
        'correct',
        {'opening_path': str, 'saving_path': str, 'nargs_base_pixel=2': int, 'nargs_correct_color=3': int},
        'Image correction with reference color',
        correct_with_reference_color
    ),
    Filter(
        'linear_stretch',
        {'opening_path': str, 'saving_path': str},
        'Linear stretching',
        linear_stretch
    ),
    Filter(
        'perfect_reflector',
        {'opening_path': str, 'saving_path': str},
        'Perfect reflector',
        perfect_reflector
    )
]
