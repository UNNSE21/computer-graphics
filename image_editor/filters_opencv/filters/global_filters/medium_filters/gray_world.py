from filters_opencv.filters.global_filters.medium_filters.utils import _calculate_mid_rgb_color
from filters_opencv.image import Image


def gray_world(image: Image):
    mid_rgb_color = _calculate_mid_rgb_color(image)
    mid_pixel_brightness = sum(mid_rgb_color) / 3
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [x / y * mid_pixel_brightness for x, y in zip(image[i, j], mid_rgb_color)]
