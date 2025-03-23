my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Original dictionary:", my_dict)

key = input("Enter key to remove: ")
if key in my_dict:
    del my_dict[key]
    print("Updated dictionary:", my_dict)
else:
    print("Key not found.")
