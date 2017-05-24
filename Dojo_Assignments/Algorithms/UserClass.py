class Bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
		self.logged = False
	def displayInfo(self):
		print("Price:", self.price)
		print("Max speed:", self.max_speed)
		print("Miles:", self.miles)
	def ride(self):
		print("Riding")
		self.miles+=10
		return self
	def reverse(self):
		if self.miles>=5:
			print("Reversing")
			self.miles-=5
		else:
			print("Already stopped")	
		return self	
		
class Car(object):
	def display_all(self):
		strout = ""
		strout = strout + " Price: " + str(self.price) + "\n"
		strout = strout + " Speed: " + str(self.speed) + "\n"
		strout = strout + " Fuel: " + str(self.fuel) + "\n"
		strout = strout + " Mileage: " + str(self.mileage) + "\n"
		strout = strout + " Tax: " + str(self.tax) + "\n"
		return strout
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if(price>10000):
			self.tax = .15
		else:
			self.tax = .12		
		print(self.display_all())
	
car1 = Car(1,2,3,4)
car2 = Car(1,2,3,4)
car3 = Car(1,2,3,4)
car4 = Car(1,2,3,4)
