class Triangle():
	def __init__(self,h,b):
		self.base = b
		self.height = h

	def area(self):
		return(0.5*self.base*self.height)

tri=Triangle(10,5)
print(tri.area())