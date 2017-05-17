class Underscore(object):
	def map(self, listy, lambday):
		g = lambday
		for counter in range(len(listy)):
			listy[counter] = g(listy[counter])
		return listy
		
	def reduce(self, lambday, listy):
		acc = listy[0]
		g = lambday	
		for counter in range(1,len(listy)):
			acc = g(acc, listy[counter])
		return acc
			
	#def find(self):
	
	#def filter(self):
	
	#def reject(self):
	
_ = Underscore()
#evens = _.filter([1,2,3,4,5,6]), lambda x: x%2 == 0)
reduceadd = _.map([1,2,3], lambda a: a*2)
print(reduceadd)


"12:01"
"12:02"
"12:00"
