def me(name, age, country, lang):
	dict = {name: "My name is "+name,
	age: "My age is "+str(age), 
	country: "My country of birth is "+country,
	lang: "My favorite lang is "+lang}
	return dict
me = me("Philip", 25, "US", "JS")
for key in me:
	print(me[key])
