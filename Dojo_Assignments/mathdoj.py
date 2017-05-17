class MathDojo(object):
	def __init__(self):
		self.total = 0
	def add(self, *arg):
		for val in arg:
			self.total+=val
		print(self.total)
		return self
	def subtract(self, *arg2):
		subtot = 0
		for val in arg2:
			subtot = self.add(arg2)
		self.total -= subtot
		return self

md = MathDojo()
md.add(2).add(2, 5).subtract(3, 2).result

class MathDojo(object):
	def __init__(self):
		self.total = 0
	def add(self, *arg):
		for val in arg:
			if type(val) is "list":
				for val2 in val:
					self.total+=val2
			else:	
				self.total+=val
		print(self.total)
		return self
