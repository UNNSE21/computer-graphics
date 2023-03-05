from filters_opencv.image import Image


def search_max_for_each_channel(image: Image):
    max_red = max_green = max_blue = 0
    for i in range(image.height):
        for j in range(image.width):
            max_red, max_green, max_blue = [max(x, image[i, j][y]) for x, y in zip(
                [max_red, max_green, max_blue],
                range(3)
            )]
    return max_red, max_green, max_blue


def search_min_for_each_channel(image: Image):
    min_red = min_green = min_blue = 0
    for i in range(image.height):
        for j in range(image.width):
            min_red, min_green, min_blue = [min(x, image[i, j][y]) for x, y in zip(
                [min_red, min_green, min_blue],
                range(3)
            )]
    return min_red, min_green, min_blue
