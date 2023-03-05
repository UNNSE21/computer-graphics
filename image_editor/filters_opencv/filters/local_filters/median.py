from copy import deepcopy

from filters_opencv.image import Image


def median(image: Image, radius: int):
    copy_image = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = _calculate_pixel_color(copy_image, j, i, radius)


def _calculate_pixel_color(image: Image, pos_x: int, pos_y: int, radius: int):
    pixels = []

    for i in range(max(0, pos_y - radius), min(image.height, pos_y + radius + 1)):
        for j in range(max(0, pos_x - radius), min(image.width, pos_x + radius + 1)):
            pixels.append((image[i, j], sum(image[i, j])))
    pixels.sort(key=lambda x: x[1])
    return pixels[len(pixels) // 2][0]
