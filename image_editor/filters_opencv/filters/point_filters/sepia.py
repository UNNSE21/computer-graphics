from filters_opencv.image import Image


def sepia(image: Image,
          coefficient: float = 20,
          rgb_percentage_ratio: tuple[float, float, float] = (0.36, 0.53, 0.11),
          ):
    if sum(rgb_percentage_ratio) != 1:
        raise "Incorrect percentage of colors. It must be exactly 1"
    for i in range(image.height):
        for j in range(image.width):
            intensity = sum([k * x for k, x in zip(rgb_percentage_ratio, image[i, j])])
            image[i, j] = [intensity + x * coefficient for x in (2, 0.5, -1)]
