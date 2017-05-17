users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
 
def parseusers(dic):
	 for key in dic:
		 count = 1
		 print(key)		 
		 for val in dic[key]:			 
			 fullname = ""
			 namelen = 0
			 for key2 in val:
				 namelen+=len(val[key2])
				 fullname= fullname+val[key2].upper()+" "			 
			 print(str(count)+" - "+fullname+"- "+str(namelen))
			 count+=1	 
		 
parseusers(users)
print(variable, end=" ")

asdfasfdasfsafasdfasd
asdfasfsd
print(variable2)
