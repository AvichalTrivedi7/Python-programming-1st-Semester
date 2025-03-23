my_set = {1, 2, 3, 4, 5}
element = int(input("Enter an element to remove: "))

if element in my_set:
    my_set.remove(element)
    print("Updated set:", my_set)
else:
    print("Element not found in the set.")
