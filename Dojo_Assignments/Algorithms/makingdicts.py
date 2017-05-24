def makingdicts(list1, list2):
	biglist = max(list1, list2, key=len)
	smalllist = min(list1, list2, key=len)
	newdict = {}
	for count in range(len(smalllist)):
		newdict[biglist[count]] = smalllist[count]
	return newdict
		
		
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "hi"]
print(makingdicts(name, favorite_animal))
