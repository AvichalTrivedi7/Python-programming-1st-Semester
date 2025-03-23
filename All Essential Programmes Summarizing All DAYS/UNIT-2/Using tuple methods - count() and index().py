my_tuple = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# Count occurrences
element = int(input("Enter element to count: "))
print(f"Occurrences of {element}:", my_tuple.count(element))

# Find index
element = int(input("Enter element to find index: "))
print(f"Index of {element}:", my_tuple.index(element))
