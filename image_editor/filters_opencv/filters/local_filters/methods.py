from filters_opencv.image import Image
BLACK_RGB = (0,0,0)
WHITE_RGB = (255,255,255)

def subtract(reduced_image: Image, deductible_image: Image):
    for i in range(reduced_image.height):
        for j in range(reduced_image.width):
            if deductible_image[i, j] == BLACK_RGB:
                reduced_image[i, j] = WHITE_RGB
