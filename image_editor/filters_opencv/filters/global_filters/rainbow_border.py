from filters_opencv.image import Image
from copy import deepcopy
from numpy import array,minimum,clip,array_equal as equal
import numpy

COLOR_BORDER = 5
SDVIG = 50

def rainbow_border(base_image:Image,sdvig:int = SDVIG,color_border:int = COLOR_BORDER):
	kernel = array([[0,1,0],[1,0,-1],[0,-1,0]])
	image = deepcopy(base_image)
	for i in range(image.height):
		for j in range(image.width):
			npc = new_pixel_color(image,i,j,kernel) 
			base_image[i,j] = minimum(
				npc + sdvig if all(npc > color_border) else 0,
				array([255,255,255]))

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