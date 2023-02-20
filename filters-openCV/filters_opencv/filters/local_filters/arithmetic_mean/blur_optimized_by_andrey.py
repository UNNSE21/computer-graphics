from copy import copy

from filters_opencv.filters.local_filters.arithmetic_mean import _arithmetic_mean
from filters_opencv.image import Image


def blur(image: Image, radius_x: int, radius_y: int):
    copy_image = copy(image)

    count_pixels = base_count_pixels = (radius_x + 1) * (radius_y + 1)
    district = base_district = [x * count_pixels for x in _arithmetic_mean(
        image,
        0,
        0,
        radius_x,
        radius_y,
    )]

    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [x / count_pixels for x in district]
            district, count_pixels = _calculate_district(copy_image, district, count_pixels, j, i, radius_x, radius_y)

        base_district, base_count_pixels = _calculate_base_district(
            copy_image,
            base_district,
            base_count_pixels,
            i,
            radius_x,
            radius_y,
        )

        district = base_district
        count_pixels = base_count_pixels


def _calculate_district(image: Image, district, count_pixels, pos_x: int, pos_y: int, radius_x: int, radius_y: int):
    for i in range(pos_y - radius_y, pos_y + radius_y + 1):
        if i < 0 or i >= image.height:
            continue
        if pos_x - radius_x < 0:
            district = [x + y for x, y in zip(district, image[i, pos_x + radius_x + 1])]
            count_pixels += 1
        elif pos_x + radius_x + 1 >= image.width:
            district = [x - y for x, y in zip(district, image[i, pos_x - radius_x])]
            count_pixels -= 1
        else:
            district = [x - y + z for x, y, z in zip(district,
                                                     image[i, pos_x - radius_x],
                                                     image[i, pos_x + radius_x + 1])]
    return district, count_pixels


def _calculate_base_district(image: Image, district, count_pixels, pos_y: int,  radius_x: int, radius_y: int):
    for j in range(radius_x + 1):
        if pos_y - radius_y < 0:
            district = [x + y for x, y in zip(district, image[pos_y + radius_y + 1, j])]
            count_pixels += 1
        elif pos_y + radius_y + 1 >= image.height:
            district = [x - y for x, y in zip(district, image[pos_y - radius_y, j])]
            count_pixels -= 1
        else:
            district = [x - y + z for x, y, z in zip(district,
                                                     image[pos_y - radius_y, j],
                                                     image[pos_y + radius_y + 1, j])]
    return district, count_pixels
