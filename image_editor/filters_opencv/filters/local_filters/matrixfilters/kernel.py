import math
from numpy import array

def create_classic_kernel(height:int,width:int):
	kernel = array([[1/(height*width)]*(width)]*height)
	return kernel

def create_gaussian_kernel(height:int,width:int,sigma:float):
	kernel = array([[0]*width]*height).astype(float)
	normal = 0.0

	for i in range(height):
		for j in range(width):
			kernel[i,j]=math.exp(-(i*i+j*j)/(sigma*sigma))
			normal+=kernel[i,j]

	for i in range(height):
		for j in range(width):
			kernel[i,j]/=normal

	return kernel
