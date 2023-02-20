from filters_opencv.filters.global_filters.median_filters.utils import _calculate_mid_rgb_color
from filters_opencv.image import Image


def average_color(image: Image, coefficient: float = 0.5):
    mid_rgb_color = _calculate_mid_rgb_color(image)
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [max(min(x + (y - x) * coefficient, 255), 0) for x, y in zip(image[i, j], mid_rgb_color)]
