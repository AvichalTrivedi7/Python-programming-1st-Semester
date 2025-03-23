def reverse_string(s):
    return s if len(s) <= 1 else s[-1] + reverse_string(s[:-1])

text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
