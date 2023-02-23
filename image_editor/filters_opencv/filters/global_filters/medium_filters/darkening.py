from filters_opencv.filters.global_filters.medium_filters.utils import _calculate_mid_rgb_color
from filters_opencv.image import Image


def darken(image: Image, coefficient: float = 1):
    mid_rgb_color = _calculate_mid_rgb_color(image)
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [max(x - y * coefficient, 0) for x, y in zip(image[i, j], mid_rgb_color)]
