from filters_opencv.filters.local_filters.dilation import dilation
from filters_opencv.filters.local_filters.erosion import erosion
from filters_opencv.image import Image
from numpy import array
BLACK_RGB = (0,0,0)
WHITE_RGB = (255,255,255)
DEFOLT_KERNEL = array(((WHITE_RGB,BLACK_RGB,WHITE_RGB),(BLACK_RGB,BLACK_RGB,BLACK_RGB),(WHITE_RGB,BLACK_RGB,WHITE_RGB)))

def closing(binary_image: Image,pattern=DEFOLT_KERNEL):
    dilation(binary_image, pattern)
    erosion(binary_image, pattern)
