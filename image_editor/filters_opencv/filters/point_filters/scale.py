from numpy import arange

from filters_opencv.image import Image


def scale(image: Image, coefficient: float):
    bitmap = []
    for i in arange(0, image.height, coefficient):
        line = []
        for j in arange(0, image.width, coefficient):
            line.append(tuple(reversed(image[int(i), int(j)])))
        bitmap.append(line)
    image.load_bitmap(bitmap)

