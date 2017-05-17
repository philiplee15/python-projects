def comparearrays(list1, list2):
	return set(list1) == set(list2)
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']
print(comparearrays(list_one, list_two))
