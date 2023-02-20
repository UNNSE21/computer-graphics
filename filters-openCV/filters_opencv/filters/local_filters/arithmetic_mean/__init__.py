from filters_opencv.image import Image


def _arithmetic_mean(image: Image, pos_x: int, pos_y: int, radius_x: int, radius_y: int):
    district = (0, 0, 0)
    count = 0
    for i in range(max(0, pos_y - radius_y), min(image.height, pos_y + radius_y + 1)):
        for j in range(max(0, pos_x - radius_x), min(image.width, pos_x + radius_x + 1)):
            district = [x + y for x, y in zip(district, image[i, j])]
            count += 1
    return [x / count for x in district]