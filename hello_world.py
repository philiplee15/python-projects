#########Quick Notes
message = "Hello World of Python"
print("\nPrint variable: " + message)
message = "What"
print("Re-assign variable and re-print: " + message)
num = 5
num2 = "apple"
#Concatting with comma to display 2 integers without adding, or int & string. 
##Concatting with + is strict for identical data types
print('Concat Multiple Data Types With ,: ', num, num2)
print("Doesn't work with a +")

##STRING CONVENTIONS
#string titling
name = "ada lovElace titling"
print("Name titled: " + name.title())
#string casing
name = "ada LOVElace casing"
print("Using upper() on a string: "+name.upper())
print("Using lower() on a string: "+name.lower())
#string concatenation
first_name = "adadada"
last_name = "lovelace"
full_name = first_name+ " " + last_name
print("Concatenate string with a + operator: "+full_name)
#whitespaces
print("Languages:\nPython\n\tC\n\t\tJavascript" + "whitespacing")
#stripping white space 
fav_lang = "python is my favorite    langauge"
print(fav_lang)
fav_lang = fav_lang.strip("")
print("Using strip() on a sequence: "+fav_lang)
print ("Roosters", 100-25*3%4)
list1 = [1,2,3,4]
print (list1*2)
##built in py string methods
#string.count(sub) - counts instances of sub within string
#string.endswith(substring) - returns boolean based upon whether last chars of string are the sub
#string.find(substring) - returns index of the start of the first occurrence of entire sub
#string.isalnum() isalpha() isdigit() isupper() - boolean test methods
#string.join(list) - returns a single string that is all strings within our sequence concatenated
#string.split() - returns a list where string is split at given delimter, without param happens at spaces
##built in py list fx (fx deal with lists outputs another)
#enumerate(sequence) - return 2 item tuple for each item in the list 1 for the index 2 for the value 
#map(function, sequence) - returns list of results
#min(sequence) - returns lowest val
#sorted(sequence) - sorts sequence
##built in py list methods (methods modify existing lists)
#list.extend(list2)
#list.pop(index) - remove item at index, default last item
#list.index(value) - return index of value

#### LOOPS
# for var in {range(x,y} || {sequence eg list, tuple, string} :
# while condition: 
# break, continue, pass
# NEW! pass - need syntax to compile but no action performs, good for testing but not production
# else statments in whiles, tricky read into it
# 





