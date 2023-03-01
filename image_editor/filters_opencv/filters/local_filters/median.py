from filters_opencv.image import Image
from copy import deepcopy
from numpy import array,sum as summ

def median(base_image:Image,h_radius:int = 3,w_radius:int = 3):
	image = deepcopy(base_image)
	for i in range(image.height):
		for j in range(image.width):
			base_image[i,j] = new_pixel_color(image,i,j,h_radius,w_radius)

def new_pixel_color(image:Image,h:int,w:int,h_radius:int,w_radius:int):
	pixels = []
	module_pixels = []
	for k in range(max(0,h-h_radius),min(h+h_radius,image.height-1)):
		for l in range(max(0,w-w_radius),min(w+w_radius,image.width-1)):
			s = summ(image[k,l])
			pixels.append((image[k,l],s))
			module_pixels.append(s)
	module_pixels.sort()
	median = module_pixels[int(len(module_pixels)/2)]

	for i in pixels:
		if i[1] == median:
			return i[0]
			
			