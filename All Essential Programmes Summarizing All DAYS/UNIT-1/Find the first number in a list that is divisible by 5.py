numbers = list(map(int, input("Enter numbers separated by space: ").split()))
for num in numbers:
    if num % 5 == 0:
        print("First number divisible by 5:", num)
        break
