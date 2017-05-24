class Call(object):
	def __init__(self, unique, name, num, time, reason):
		self.unique = unique
		self.name = name
		self.num = num
		self.time = time
		self.reason = reason
	def display(self):
		listy = [a for a in dir(self) if not a.startswith('__') if a != "display"]
		for val in listy:
			print(val.title()+":", getattr(self, val))
		print("\n")

class CallCenter(object):
	def __init__(self, calls):
		self.calls = calls
		self.queue = len(calls)
	def add(self, call):
		self.calls.append(call)
		self.queue+=1
	def remove(self):
		del self.calls[0]		
		self.queue-=1
		return self		
	def info(self):
		for val in self.calls:
			print("Name:"+val.name)
			print("Phone Number:"+str(val.num)+"\n")
		print("There are {} call(s) in the queue".format(self.queue))
			
	def removenumber(self, number):
		for count in range(len(self.calls)-1):
			if self.calls[count].num == number:				
				del self.calls[count]
						
c  = Call("abc", "Mike", 9099224649, "12:01" , "die")
c1 = Call("abcd", "Mikee", 9099224648, "12:02", "die")
c2 = Call("abce", "Mikeee", 9099224647, "12:03", "die")
c3 = Call("abcf", "Mikeeee", 9099224646, "12:04", "die")

c.display()
calllist = [c, c1, c2, c3]
center = CallCenter(calllist) 
center.info()
center.remove()
center.add(c3)
center.removenumber(9099224648)

