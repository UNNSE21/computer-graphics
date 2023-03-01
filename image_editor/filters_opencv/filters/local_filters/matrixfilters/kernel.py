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

def create_motion_kernel(matrix_size:int):
	a=array([[0]*matrix_size]*matrix_size).astype(float)
	for i in range(matrix_size):
		a[i,i]=1
	a*=(1/matrix_size)
	return a

def create_sharp_kernel():
	return array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

#border filters_kernel

def create_sobel_kernel():
	x =array([[-1,0,1],[-2,0,2],[-1,0,1]])
	y = array([[-1,-2,-1],[0,0,0],[1,2,1]])
	return (x,y)

def create_scharr_kernel():
	y = array([[3,10,3],[0,0,0],[-3,-10,-3]])
	x = array([[3,0,-3],[10,0,-10],[3,0,-3]])
	return (x,y)

def create_pruitt_kernel():
	y = array([[1,1,1],[0,0,0],[-1,-1,-1]])
	x = array([[1,0,-1],[1,0,-1],[1,0,-1]])
	return (x,y)

