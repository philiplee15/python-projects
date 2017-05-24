
def oddeven():
	for count in range(1,2000):
		print("Number is ", count, end=". ")
		if count%2 == 0:
			print("This is an even number.")
		elif count%2 == 1:
			print("This is an odd number.")
oddeven()

a = [2,4,10,16]
def multiple(list, num):
	for counter in range(0,len(list)):
		list[counter]*=num
	return list
print(multiple(a, 5))

def layered_mults(list):
	layer = []
	for val in list:
		store = []
		for count in range(val):
			store.append(1)
		layer.append(store)
	return layer	
		
x = layered_mults(multiple([2,4,5],3))
print(x)
