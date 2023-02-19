from filters_opencv.image import Image


def darken(image: Image, coefficient: float = 1):
    mid_rgb_color = _calculate_mid_rgb_color(image)
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [max(x - y * coefficient, 0) for x, y in zip(image[i, j], mid_rgb_color)]


def lighten(image: Image, coefficient: float = 1):
    mid_rgb_color = _calculate_mid_rgb_color(image)
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [min(x + y * coefficient, 255) for x, y in zip(image[i, j], mid_rgb_color)]


def average_color(image: Image, coefficient: float = 0.5):
    mid_rgb_color = _calculate_mid_rgb_color(image)
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [max(min(x + (y - x) * coefficient, 255), 0) for x, y in zip(image[i, j], mid_rgb_color)]


def _calculate_mid_rgb_color(image: Image):
    sum_rgb_color = (0, 0, 0)
    for i in range(image.height):
        for j in range(image.width):
            sum_rgb_color = [x + y for x, y in zip(sum_rgb_color, image[i, j])]

    return [x / image.size for x in sum_rgb_color]
