words = input("Enter words separated by space: ").split()
word_length_dict = {word: len(word) for word in words}
print("Dictionary of words and their lengths:", word_length_dict)
