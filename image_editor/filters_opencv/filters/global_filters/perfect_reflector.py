from filters_opencv.filters.global_filters.utils.methods import search_max_for_each_channel
from filters_opencv.image import Image


def perfect_reflector(image: Image):
    max_red, max_green, max_blue = search_max_for_each_channel(image)
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [x / y * 255 for x, y in zip(image[i, j], [max_red, max_green, max_blue])]
