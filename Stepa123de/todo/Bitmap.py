from PIL import Image
import numpy as np

class Bitmap:
	def __init__(self,dir:str):
		try:
			image = Image.open(dir);
			self.width = image.width;
			self.height = image.height;
		except:
			print("Exeption can't Image.open(dir)")

		newBitmap = np.asarray(image);
		self.Bitmap = newBitmap.copy();
		self.Bitmap.tolist();

	def __getitem__(self,pos):
		x,y = pos
		return self.Bitmap[y,x];

	def __setitem__(self, pos, rgb): #rgb array [r, g, b]
		x,y = pos
		self.Bitmap[y,x]=rgb

	def show(self):
		image = Image.fromarray(self.Bitmap);
		image.show();

	def scale2(self,scale:int):
		newImage = []
		for y in range(0,self.height,scale):
			imageLine = []
			for x in range(0,self.width,scale):
				imageLine.append(self.Bitmap[y,x]);
			newImage.append(imageLine)
		self.Bitmap = np.asarray(newImage)