#Write code that prints all odd nums 1-1000
def print1tothou():
	for count in range(1,1000):
		if (count%2) == 1:
			print(count)
print1tothou()

#Create another "program" print all mult of 5, 5-1000000
def print5tomil():
	for count in range (5,1000000):
		if count%5 == 0:
			print(count)

#Create prog that prints sum of all values in list
a = [1, 2, 5, 10, 255, 3]
def sumoflist(list):
	count2 = 0
	for val in list:
		count2+=val
	return count2
print(sumoflist(a))
		
#Sum avg program
def avglist(list):
	return sumoflist(list)/len(list)
print(avglist(a))
