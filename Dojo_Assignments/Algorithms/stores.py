from Products import Product

class Store(Product):
	def __init__(self, products, location, owner):
		self.products = products
		self.location = location
		self.owner = owner
	def add_product(self, newprod):
		for val in self.products:
			if val.item_name == newprod:
				self.products.append(newprod)
		return self
	def remove_product(self, removes):
		for val in self.products:
			if val.item_name == removes:
				del val
		return self
	def inventory(self):
		for val in self.products:
			val.dispall()
		return self
		
product0 = Product()
product1 = Product()
product2 = Product()
product3 = Product()
product4 = Product()
prodarray = [product0, product1, product2, product3, product4]

store = Store(prodarray, "Africa", "Me")
store.remove_product("Item")
print(store.products)

