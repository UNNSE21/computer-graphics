from Bitmap import Bitmap


bitmap = Bitmap("files/img.jpg")
'''
for x in range(bitmap.width):
	for y in range(bitmap.height):
		a = bitmap[x,y]
		for i in range(len(a)):
			a[i]=255-a[i]
		bitmap[x,y] = a
'''

bitmap.scale2(2)

bitmap.show()