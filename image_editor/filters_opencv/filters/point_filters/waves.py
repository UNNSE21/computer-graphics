from filters_opencv.image import Image
from copy import deepcopy
from math import sin,pi

def waves_index_first(h:int,w:int):
	new_x = h + 20*sin(2*pi*w/60)
	new_y = w

	return (int(new_x),int(new_y))

def waves_index_second(h:int,w:int):
	new_x = h + 20*sin(2*pi*h/30)
	new_y = w

	return (int(new_x),int(new_y))


def _base_filter(base_image:Image,func):
	image = deepcopy(base_image)
	for i in range(image.height):
		for j in range(image.width):
			x,y = func(i,j)
			if(x >= 0 and x < image.height and y >= 0 and y <image.width):
				base_image[i,j] = image[x,y]
			else:
				base_image[i,j] = (0,0,0)#black

def waves(base_image:Image,var1 = True):
	if(var1):
		_base_filter(base_image,waves_index_first)
	else:
		_base_filter(base_image,waves_index_second)