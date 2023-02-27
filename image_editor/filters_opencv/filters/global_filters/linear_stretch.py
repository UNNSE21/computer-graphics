from filters_opencv.image import Image
from numpy import maximum, minimum, array

def rgb_extremes(image:Image):
	rgb_min = image[0,0]
	rgb_max = image[0,0]

	for i in range(image.height):
		for j in range(image.width):
			rgb_min = minimum(rgb_min, image[i, j])
			rgb_max = maximum(rgb_max, image[i, j])

	return rgb_min,rgb_max

def linear_stretch(image:Image):
	rgb_min,rgb_max = rgb_extremes(image)

	for i in range(image.height):
		for j in range(image.width):
			image[i,j] = (image[i,j]-rgb_min)*(255/(rgb_max-rgb_min))