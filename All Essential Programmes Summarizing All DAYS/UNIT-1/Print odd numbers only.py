numbers = list(map(int, input("Enter numbers separated by space: ").split()))
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)
