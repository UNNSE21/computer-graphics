from copy import copy

from filters_opencv.filters.local_filters.arithmetic_mean import _arithmetic_mean
from filters_opencv.image import Image


def blur(image: Image, radius_x: int, radius_y: int):
    copy_image = copy(image)
    district_height = 2 * radius_y + 1
    district_width = 2 * radius_x + 1
    district_size = district_width * district_height

    district = base_district = [x * district_size for x in _arithmetic_mean(
        image,
        radius_x,
        radius_y,
        radius_x,
        radius_y,
    )]

    for i in range(image.height):
        for j in range(image.width):
            if i < radius_y or i + radius_y + 2 > image.height or j < radius_x or j + radius_x + 2 > image.width:
                image[i, j] = _arithmetic_mean(copy_image, j, i, radius_x, radius_y)
            else:
                image[i, j] = [x / district_size for x in district]
                district = _calculate_district(copy_image, district, j, i, radius_x, radius_y)

        if i >= radius_y and i + radius_y + 2 <= image.height:
            base_district = _calculate_base_district(copy_image, base_district, i, district_width, radius_y)
            district = base_district


def _calculate_district(image: Image, district, pos_x: int, pos_y: int, radius_x: int, radius_y: int):
    for i in range(pos_y - radius_y, pos_y + radius_y + 1):
        district = [x - y + z for x, y, z in zip(district,
                                                 image[i, pos_x - radius_x],
                                                 image[i, pos_x + radius_x + 1])]
    return district


def _calculate_base_district(image: Image, district, pos_y: int,  district_width: int, radius_y: int):
    for j in range(district_width):
        district = [x - y + z for x, y, z in zip(district,
                                                 image[pos_y - radius_y, j],
                                                 image[pos_y + radius_y + 1, j])]
    return district
