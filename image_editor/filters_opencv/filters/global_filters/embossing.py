from filters_opencv.image import Image
from copy import deepcopy
#from filters_opencv.filters.local_filters.matrixfilters.new_pixel_color import new_pixel_color
#from filters_opencv.filters.local_filters.matrixfilters.kernel import *
from numpy import array,minimum,clip,sum as summ
import numpy


def embossing(base_image:Image):
	kernel = array([[0,1,0],[1,0,-1],[0,-1,0]])
	image = deepcopy(base_image)
	koef_sdvig = 100
	for i in range(image.height):
		for j in range(image.width):
			base_image[i,j] = minimum(new_pixel_color(image,i,j,kernel) + koef_sdvig,array([255,255,255]))

	#normolize(base_image)


def normolize(image:Image,radius:int=10):
	mid_rgb = array([0.0,0.0,0.0])
	for i in range(image.height):
		for j in range(image.width):
			mid_rgb+=image[i,j]

	mid_rgb/=(image.height*image.width)
	l = mid_rgb - radius
	r = mid_rgb + radius

	for i in range(image.height):
		for j in range(image.width):
			image[i,j]=clip(image[i,j],l,r)

def clamp(value,minn,maxx):
	if(value<minn):
		return minn
	elif(value>maxx):
		return maxx
	else:
		return value

def new_pixel_color(image:Image,h:int,w:int,kernel):
	result_rgb=array([0,0,0])

	radius_h = int(len(kernel)/2)
	radius_w = int(len(kernel[0])/2)

	for i in range(-radius_h,radius_h + 1):
		for j in range(-radius_w,radius_w + 1):
			ind_i=clamp(h+i,0,image.height-1)
			ind_j=clamp(w+j,0,image.width-1)
			result_rgb[0]+=image[ind_i,ind_j][0]*kernel[i+radius_h,j+radius_w]
			result_rgb[1]+=image[ind_i,ind_j][1]*kernel[i+radius_h,j+radius_w]
			result_rgb[2]+=image[ind_i,ind_j][2]*kernel[i+radius_h,j+radius_w]

	return result_rgb.astype(int)