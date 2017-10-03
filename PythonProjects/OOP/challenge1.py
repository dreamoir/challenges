
class Apple():
	def __init__(self,w,s,c,j):
		''' weight is is kgs, size is volume (m^3),
		colour is color, juice is moisture content (%)  '''
		self.weight = w
		self.size = s
		self.colour = c
		self.juice = j

	def density(self):
		return(self.weight/self.size)

	def water(self,d):
		return(d*self.juice)
		


apple = Apple(10,2,"red",0.5)

d=apple.density()
print(d)
print(apple.colour)
print(apple.water(d))

