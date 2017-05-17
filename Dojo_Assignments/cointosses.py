import random

def cointoss5000():
	head = 0
	tail = 0
	for count in range(1,5001):
		rand = round(random.randint(0, 1))
		coin="landed on the middle"
		if rand == 1:
			head+=1
			coin = "head"
		else:
			tail+=1
			coin = "tail"
		print("Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(count, coin, head, tail))
		
cointoss5000()
