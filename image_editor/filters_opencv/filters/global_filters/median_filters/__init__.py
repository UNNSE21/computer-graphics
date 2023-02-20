from filters_opencv.image import Image


def _calculate_mid_rgb_color(image: Image):
    sum_rgb_color = (0, 0, 0)
    for i in range(image.height):
        for j in range(image.width):
            sum_rgb_color = [x + y for x, y in zip(sum_rgb_color, image[i, j])]

    return [x / image.size for x in sum_rgb_color]
