def stars(list):
	for val in list:
		if type(val) == str:
			word = ""
			for count in range(len(val)):
				word+=val[0].lower()
			print(word)
		elif type(val) == int: 
			word = ""
			for count in range(val):
				word+="*"
			print(word)
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(x)
