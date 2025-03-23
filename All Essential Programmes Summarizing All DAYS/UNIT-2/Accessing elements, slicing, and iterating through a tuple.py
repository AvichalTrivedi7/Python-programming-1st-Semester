my_tuple = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Sliced tuple:", my_tuple[1:4])

# Iterating
print("Iterating through tuple:")
for item in my_tuple:
    print(item, end=" ")
print()
