my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Using dictionary methods
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

key = input("Enter key to retrieve value: ")
print("Value:", my_dict.get(key, "Key not found"))
