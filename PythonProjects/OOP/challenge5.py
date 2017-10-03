class Shape:
	def what_am_i(self):
		print("I am a Shape")

class Rectangle(Shape):
	def __init__(self,w,l):
		self.width = w
		self.length = l

	def calculate_perimeter(self):
		return 2*(self.width+self.length)



class Square(Shape):
	def __init__(self,l):
		self.length = l

	def calculate_perimeter(self):
		return 4*self.length

	def change_size(self,x):
		self.length += x	

rect=Rectangle(4,5)
sq=Square(5)
sq.change_size(-4)

print(rect.calculate_perimeter())
print(sq.calculate_perimeter())
print(rect.what_am_i())
print(sq.what_am_i())

