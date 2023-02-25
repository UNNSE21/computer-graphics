from filters_opencv.image import Image


def change_brightness(image: Image, delta: int):
    for i in range(image.height):
        for j in range(image.width):
            image[i, j] = [x + delta for x in (image[i, j])]
