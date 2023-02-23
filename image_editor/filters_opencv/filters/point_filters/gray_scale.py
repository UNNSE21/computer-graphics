from filters_opencv.image import Image


def gray_scale(image: Image,
               rgb_percentage_ratio: tuple[float, float, float] = (0.36, 0.53, 0.11),
               ):
    if sum(rgb_percentage_ratio) != 1:
        raise "Incorrect percentage of colors. It must be exactly 1"
    for i in range(image.height):
        for j in range(image.width):
            intensity = sum([k * x for k, x in zip(rgb_percentage_ratio, image[i, j])])
            image[i, j] = [intensity, intensity, intensity]
