print("x", end=" ")
for x in range(1,13): 
	if x == 12:
		print(x)
	else:
		print(x, end=" ")
for row in range(1,13):
	print(row, end=" ")
	for col in range(1,13):
		if col == 12:
			print(col*row)
		else:
			print(col*row, end=" ")
		
