
def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True
def foobar():
	for i in range(100, 100001):
		if isprime(i):
			print(i, ": Foo")
		elif (i**.5 ).is_integer():
			print(i, ": Bar")
		else:
			print(i, ": Food Bar")
foobar()
