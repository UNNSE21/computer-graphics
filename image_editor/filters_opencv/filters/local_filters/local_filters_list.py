from typing import Final

from filters_opencv.filters import *
from filters_opencv.filters.filter import Filter

local_filters: Final = [
    Filter(
        'blur',
        {'opening_path': str, 'saving_path': str, 'radius_x': int, 'radius_y': int},
        'Blur image',
        blur_by_andrey
    ),
    Filter(
        'blur_gaussian',
        {'opening_path': str, 'saving_path': str, 'sigma': float, 'nargs_size=?': int},
        'Blur by gaussian images',
        blur_gaussian
    ),
    Filter(
        'motion_blur',
        {'opening_path': str, 'saving_path': str, 'size': int},
        'Blurring the image when the camera is rotated',
        motion_blur
    ),
    Filter('pruitt', {'opening_path': str, 'saving_path': str}, 'Pruitt boundary allocation', pruitt),
    Filter('sharra', {'opening_path': str, 'saving_path': str}, 'Sharra boundary allocation', sharra),
    Filter('sobel', {'opening_path': str, 'saving_path': str}, 'Sobel boundary allocation', sobel),
    Filter(
        'dilation',
        {'opening_path': str, 'saving_path': str, 'nargs_path_pattern=?': str, 'nargs_base_pixel=*': int},
        'Mathematical Morphology operation',
        dilation
    ),
    Filter(
        'erosion',
        {'opening_path': str, 'saving_path': str, 'nargs_path_pattern=?': str, 'nargs_base_pixel=*': int},
        'Mathematical Morphology operation',
        erosion
    ),
    Filter(
        'opening',
        {'opening_path': str, 'saving_path': str, 'nargs_path_pattern=?': str, 'nargs_base_pixel=*': int},
        'Mathematical Morphology operation',
        opening
    ),
    Filter(
        'closing',
        {'opening_path': str, 'saving_path': str, 'nargs_path_pattern=?': str, 'nargs_base_pixel=*': int},
        'Mathematical Morphology operation',
        closing
    ),
    Filter(
        'black_hat',
        {'opening_path': str, 'saving_path': str, 'nargs_path_pattern=?': str, 'nargs_base_pixel=*': int},
        'Mathematical Morphology operation',
        black_hat
    ),
    Filter(
        'top_hat',
        {'opening_path': str, 'saving_path': str, 'nargs_path_pattern=?': str, 'nargs_base_pixel=*': int},
        'Mathematical Morphology operation',
        top_hat
    ),
    Filter(
        'grad',
        {'opening_path': str, 'saving_path': str, 'nargs_path_pattern=?': str, 'nargs_base_pixel=*': int},
        'Mathematical Morphology operation',
        grad
    ),
    Filter('emboss', {'opening_path': str, 'saving_path': str}, 'Image embossing', emboss),
    Filter(
        'glowing_edges',
        {'opening_path': str, 'saving_path': str, 'radius_filter': int},
        'Highlighting the borders of objects',
        glowing_edges
    ),
    Filter(
        'increase_sharpness_1',
        {'opening_path': str, 'saving_path': str},
        'Increase the sharpness (method 1)',
        increase_sharpness_1
    ),
    Filter(
        'increase_sharpness_2',
        {'opening_path': str, 'saving_path': str},
        'Increase the sharpness (method 2)',
        increase_sharpness_2
    ),
    Filter('maximum', {'opening_path': str, 'saving_path': str, 'radius': int}, 'Maximum filter', maximum),
    Filter('median', {'opening_path': str, 'saving_path': str, 'radius': int}, 'Median filter', median),

]
