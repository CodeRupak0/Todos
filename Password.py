password= input("Enter a Password: ")
result={}    #defining dictionary so that we could assign values to the array
if len(password) >= 8:
    result["Length"]=True  #defining the keys of the dictionaries
else:
    result["Length"]=False   #defining the keys of the dictionaries
digit= False
for i in password:
    if i.isdigit():
        digit=True
result["digit"]= digit    #defining the keys of the dictionaries
uppercase= False
for i in password:
    if i.isupper():
        uppercase=True
result["uppercase"]=uppercase   #defining the keys of the dictionaries
print (result)
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")

