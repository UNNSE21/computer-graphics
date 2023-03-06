from filters_opencv.image import Image


def correct_with_reference_color(image: Image, base_pixel: tuple[int, int], correct_color: tuple[int, int, int]):
    base_pixel = tuple(base_pixel)
    base_pixel_color = image[base_pixel]
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [x * y / z for x, y, z in zip(
                image[i, j],
                correct_color,
                base_pixel_color
            )]
