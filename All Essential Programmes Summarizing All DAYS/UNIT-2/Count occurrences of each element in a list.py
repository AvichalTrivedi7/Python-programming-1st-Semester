from collections import Counter

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
count = Counter(numbers)
print("Occurrences:", dict(count))
