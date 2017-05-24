import random
print("Scorse and Grades")
for count in range(11):	
	rand = random.randint(60, 100)
	print("Score: ", rand,";", "Your grade is ", end="")
	if rand>=90:
		print("A")
	elif rand>=80:
		print("B")
	elif rand>=70:
		print("C")
	elif rand>=60:
		print("D")

