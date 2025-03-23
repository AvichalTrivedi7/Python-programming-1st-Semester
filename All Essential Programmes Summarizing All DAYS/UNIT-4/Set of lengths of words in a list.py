words = input("Enter words separated by space: ").split()
length_set = {len(word) for word in words}
print("Set of word lengths:", length_set)
