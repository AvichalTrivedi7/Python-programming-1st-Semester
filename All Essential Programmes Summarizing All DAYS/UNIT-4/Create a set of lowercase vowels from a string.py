text = input("Enter a string: ").lower()
vowels = {char for char in text if char in "aeiou"}
print("Lowercase vowels in the string:", vowels)
