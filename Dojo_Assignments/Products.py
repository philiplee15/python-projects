class Product(object):
	def __init__(self, price=5, item_name="Item", weight=5, brand="Brand", cost=5, status="For Sale"):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = "For Sale"
	def sell(self):
		self.status = "Sold"
		return self
	def addTax(self, tax):
		return self.price*tax + self.price
	def Return(self, reason):
		if reason=="defective":
			self.status = "defective"
			self.price = 0
		elif reason=="open":
			self.status = "for sale"
			self.price = self.price*.8
		elif reason=="like new":
			self.status = "for sale"		
		return self
	def dispall(self):
		print("Price:", self.price) 
		print("Item Name:", self.item_name) 
		print("Weight:", self.weight) 
		print("Brand:", self.brand) 
		print("Cost:", self.cost) 
		print("Status:", self.status) 

		

		
		
		
