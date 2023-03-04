from copy import deepcopy
from filters_opencv.filters.local_filters.erosion import erosion
from filters_opencv.filters.local_filters.methods import subtract
from filters_opencv.image import Image
from numpy import array
BLACK_RGB = (0,0,0)
WHITE_RGB = (255,255,255)
DEFOLT_KERNEL = array(((WHITE_RGB,BLACK_RGB,WHITE_RGB),(BLACK_RGB,BLACK_RGB,BLACK_RGB),(WHITE_RGB,BLACK_RGB,WHITE_RGB)))

def top_hat(binary_image: Image, pattern=DEFOLT_KERNEL):
    copy_image = deepcopy(binary_image)
    erosion(copy_image, pattern)
    subtract(binary_image, copy_image)

