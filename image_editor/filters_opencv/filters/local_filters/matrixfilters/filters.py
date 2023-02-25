from filters_opencv.image import Image
from copy import deepcopy
from filters_opencv.filters.local_filters.matrixfilters.new_pixel_color import new_pixel_color
from filters_opencv.filters.local_filters.matrixfilters.kernel import *

def matrix_blur(base_image:Image,h_matrix:int,w_matrix:int):
	image = deepcopy(base_image)
	kernel = create_classic_kernel(h_matrix,w_matrix)
	for i in range(image.height):
		for j in range(image.width):
			base_image[i,j]=new_pixel_color(image,i,j,kernel)

def matrix_gaussian_blur(base_image:Image,h_matrix:int,w_matrix:int,sigma):
	image = deepcopy(base_image)
	kernel = create_gaussian_kernel(h_matrix,w_matrix,sigma)
	for i in range(image.height):
		for j in range(image.width):
			base_image[i,j]=new_pixel_color(image,i,j,kernel)
