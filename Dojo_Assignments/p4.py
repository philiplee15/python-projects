def typelist(list):
	tot = 0
	intchange = 0
	strchange = 0
	thetype = "mixed"
	for x in list:
		if type(x) is int:
			tot+=x
			thetype = "int"
			intchange+=1
		elif type(x) is str: 
			thetype = "str"
			strchange+=1
			print("String: " + x)
		if intchange>0 and strchange>0:
			thetype="mixed"
	print("The array you entered is of "+thetype+" type") 
	if tot>0:
		print("Sum: ",tot)
l = ['magical','unicorns']
typelist(l)
