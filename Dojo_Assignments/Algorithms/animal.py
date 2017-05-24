class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health-=1
		return self
	def run(self):
		self.health-=5
		return self
	def displayHealth(self):
		print(self.name+":", self.health)
		return self
animal = Animal("animal")
animal.walk().walk().walk().run().run().displayHealth()
	
class Dog(Animal):
	def __init__(self):
		super(Dog, self).__init__()
		self.health = 150
	def pet(self):
		self.health+=5
		return self

dog = Dog("test")
dog.pet().run().run().walk().displayHealth()


class Dragon(Animal):
	def __init__(self):
		self.name = "dragon"
		self.health = 170
	def fly(self):
		self.health-=10
		return self
	def displayHealth(self):	
		print("I'm a moflippin' dragon mofluppa")
		super(Dragon, self).displayHealth()
		return self
dragon = Dragon()
dragon.fly().walk().run().run().displayHealth()
