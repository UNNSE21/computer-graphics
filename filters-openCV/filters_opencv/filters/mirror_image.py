from filters_opencv.image import Image


def horizontally(image: Image):
    for i in range(image.height):
        for j in range(int(image.width / 2)):
            image[i, j], image[i, image.width - 1 - j] = image[i, image.width - 1 - j],  image[i, j]


def vertically(image: Image):
    for i in range(int(image.height / 2)):
        for j in range(image.width):
            image[i, j], image[image.height - 1 - i, j] = image[image.height - 1 - i, j],  image[i, j]
