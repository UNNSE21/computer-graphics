from filters_opencv.image import Image
from numpy import array,clip

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