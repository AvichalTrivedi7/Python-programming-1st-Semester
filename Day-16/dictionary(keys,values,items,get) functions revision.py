dict1={1:"a",2:"b",3:"c","Hi":"Greetings"}

for i in dict1.keys():

    print(i)

for x in dict1.values():

    print(x)

for a,b in dict1.items():

    print(a,b)
    

ValueToFind=input("Enter the value you want to get from dictionary: ")

if ValueToFind.isdigit():

    ValueToFind=int(ValueToFind)

print(dict1.get(ValueToFind,"NoSuchValue"))


