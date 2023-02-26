from random import random
from filters_opencv.image import Image
from copy import deepcopy

def glass_index(h:int,w:int):
	new_x = h + (random()-0.5)*10
	new_y = w + (random()-0.5)*10

	return (int(new_x),int(new_y))

def glass(base_image:Image):
	image = deepcopy(base_image)
	for i in range(image.height):
		for j in range(image.width):
			x,y = glass_index(i,j)
			if(x >= 0 and x < image.height and y >= 0 and y <image.width):
				base_image[i,j] = image[x,y]