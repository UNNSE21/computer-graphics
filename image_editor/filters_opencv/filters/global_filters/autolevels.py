from filters_opencv.filters.global_filters.utils.methods import (search_max_for_each_channel,
                                                                 search_min_for_each_channel,
                                                                 )
from filters_opencv.image import Image


def autolevels(image: Image):
    max_red, max_green, max_blue = search_max_for_each_channel(image)
    min_red, min_green, min_blue = search_min_for_each_channel(image)
    for i in range(image.height):
        for j in range(image.width):
            t = image[i, j]
            image[i, j] = [(x - y) / (z - y) * 255 for x, y, z in zip(
                image[i, j],
                [min_red, min_green, min_blue],
                [max_red, max_green, max_blue]
            )]
