from copy import deepcopy

from filters_opencv.filters.local_filters.utils.constants import EMBOSSING_KERNEL
from filters_opencv.filters.local_filters.utils.kernel_application import calculate_pixel_color
from filters_opencv.image import Image


def emboss(image: Image):
    copy_image = deepcopy(image)
    for i in range(image.height):
        for j in range(image.width):
            pixel = [x + 128 for x in calculate_pixel_color(copy_image, j, i, EMBOSSING_KERNEL)]
            pixel = pixel if all([x <= 255 for x in pixel]) else [255, 255, 255]
            image[i, j] = pixel
