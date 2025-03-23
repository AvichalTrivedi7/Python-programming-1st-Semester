tuple1 = tuple(map(int, input("Enter first tuple elements separated by space: ").split()))
tuple2 = tuple(map(int, input("Enter second tuple elements separated by space: ").split()))

# Concatenation
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Repetition
print("Repeated Tuple:", tuple1 * 2)

# Membership Test
element = int(input("Enter element to check: "))
print("Exists in tuple?", element in tuple1)
