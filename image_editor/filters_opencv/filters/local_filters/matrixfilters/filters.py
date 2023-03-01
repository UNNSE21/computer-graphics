from filters_opencv.image import Image
from copy import deepcopy
from filters_opencv.filters.local_filters.matrixfilters.new_pixel_color import new_pixel_color
from filters_opencv.filters.local_filters.matrixfilters.kernel import *
from numpy import abs,minimum

def _basic_matrix(base_image:Image,kernel):
	image = deepcopy(base_image)
	for i in range(image.height):
		for j in range(image.width):
			base_image[i,j] = new_pixel_color(image,i,j,kernel)

def matrix_blur(base_image:Image,h_matrix:int,w_matrix:int):
	_basic_matrix(base_image,create_classic_kernel(h_matrix,w_matrix))

def matrix_gaussian_blur(base_image:Image,h_matrix:int,w_matrix:int,sigma):
	_basic_matrix(base_image,create_gaussian_kernel(h_matrix,w_matrix,sigma))

def matrix_motion_blur(base_image:Image,matrix_size:int):
	_basic_matrix(base_image,create_motion_kernel(matrix_size))

def matrix_sharp(base_image:Image):
	_basic_matrix(base_image,create_sharp_kernel())

def _basic_matrix_border(base_image:Image,kernel):
	image = deepcopy(base_image)
	kernel_x,kernel_y = kernel
	for i in range(image.height):
		for j in range(image.width):
			base_image[i,j]=abs(new_pixel_color(image,i,j,kernel_x))+abs(new_pixel_color(image,i,j,kernel_y))

# border filters
def matrix_sobel(base_image:Image):
	_basic_matrix_border(base_image,create_sobel_kernel()) 

def matrix_scharr(base_image:Image):
	_basic_matrix_border(base_image,create_scharr_kernel())

def matrix_pruitt(base_image:Image):
	_basic_matrix_border(base_image,create_pruitt_kernel())