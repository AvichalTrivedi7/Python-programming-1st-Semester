dict1={1:"a",2:"b",3:"c","Hi":"Greetings"}



ValueToRemove=input("Please enter the value you want to remove: ")

if ValueToRemove.isdigit():

    ValueToRemove=int(ValueToRemove)

print("You have removed: ",dict1.pop(ValueToRemove,"NoSuchValue"))


del dict1[2]

print(f"dictionary after using pop and del: {dict1}")


dict1.clear()

print(f"Emptied dictionary: {dict1}")

