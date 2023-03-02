from filters_opencv.image import Image
from copy import deepcopy
from numpy import array,array_equal as equal

BLACK_RGB = array((0,0,0))
WHITE_RGB = array((255,255,255))

DEFOLT_KERNEL = array(((WHITE_RGB,BLACK_RGB,WHITE_RGB),(BLACK_RGB,BLACK_RGB,BLACK_RGB),(WHITE_RGB,BLACK_RGB,WHITE_RGB)))

def dilation(base_image:Image,kernel=DEFOLT_KERNEL):
	image = deepcopy(base_image)
	for i in range(image.width):
		for j in range(image.height):
			if(equal(image[i,j],BLACK_RGB)):
				pixels(base_image,image,i,j,kernel)

def pixels(base_image:Image,image:Image,h:int,w:int,kernel):
	rad_h = int(len(kernel)/(2))
	rad_w = int(len(kernel[0])/(2))
	for k in range(max(0,h-rad_h),min(image.height-1,h+rad_h)):
		for l in range(max(0,w-rad_w),min(image.width-1,w+rad_w)):
			if(equal(kernel[h+rad_h-k,w+rad_w-l],BLACK_RGB)):
				base_image[k,l] = BLACK_RGB