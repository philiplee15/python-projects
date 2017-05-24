def findchars(char, n):
	a=[]
	for val in n:
		if char in val:
			a.append(val)
	return a
l = ['hello','world','my','name','is','Anna']
char = 'o'
print(findchars(char, l))
	
