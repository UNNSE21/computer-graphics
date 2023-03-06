from filters_opencv.filters import *
from filters_opencv.filters.filter import Filter

filters = [
    Filter('mirror_horizontally', ['opening_path', 'saving_path'], 'Horizontal mirror image', horizontally),
    Filter('mirror_vertically', ['opening_path', 'saving_path'], 'Vertically mirror image', vertically),
    Filter(
        'relocate',
        ['opening_path', 'saving_path', 'offset_x', 'offset_y'],
        'Transfer images by the certain number of pixels',
        relocate
    ),
    Filter(
        'rotation',
        ['opening_path', 'saving_path', 'center_x', 'center_y', 'angle_rotation'],
        'Rotates images relative to the certain pixel by the certain angle',
        rotate
    ),
    Filter('scale', ['opening_path', 'saving_path', 'coefficient'], 'Changes the size of the image', scale),
    Filter(
        'change_brightness',
        ['opening_path', 'saving_path', 'delta'],
        'Changes the brightness of the image by a certain number',
        change_brightness
    ),
    Filter('glass_effect', ['opening_path', 'saving_path'], 'Applies the glass effect to the image', glass_effect),
    Filter('gray_scale', ['opening_path', 'saving_path'], 'Makes the image in grayscale', gray_scale),
    # Filter(
    #     'gray_scale_1',
    #     ['opening_path', 'saving_path', 'rgb_percentage_ratio'],
    #     'Makes an image in grayscale with a certain percentage for each color',
    #     gray_scale
    # ),
    Filter('invert', ['opening_path', 'saving_path'], 'Inverts the image', invert),
    Filter('sepia', ['opening_path', 'saving_path'], 'Applies a sepia effect to the image', sepia),
    Filter(
        'sepia_1',
        ['opening_path', 'saving_path', 'coefficient'],
        'Applies a sepia effect with a certain coefficient to the image',
        sepia
    ),
    # Filter(
    #     'sepia_2',
    #     ['opening_path', 'saving_path', 'coefficient', 'rgb_percentage_ratio'],
    #     'Applies a sepia effect with a certain coefficient and a certain percentage for each color to the image',
    #     sepia
    # ),
    Filter(
        'waves',
        ['opening_path', 'saving_path', 'direction'],
        'Applies the effect of waves in a certain direction (vertical, horizontal) to the image',
        waves
    ),
]
