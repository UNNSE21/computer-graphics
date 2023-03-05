from copy import deepcopy

from filters_opencv.image import Image


def maximum(image: Image, radius):
    copy_image = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = _calculate_pixel_color(copy_image, j, i, radius)


def _calculate_pixel_color(image: Image, pos_x: int, pos_y: int, radius: int):
    max_red = max_green = max_blue = 0
    for i in range(max(0, pos_y - radius), min(image.height, pos_y + radius + 1)):
        for j in range(max(0, pos_x - radius), min(image.width, pos_x + radius + 1)):
            max_red, max_green, max_blue = [max(x, image[i, j][y]) for x, y in zip(
                [max_red, max_green, max_blue],
                range(3)
            )]
    return max_red, max_green, max_blue
