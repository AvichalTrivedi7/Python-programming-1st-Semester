def list_sum(lst):
    return 0 if not lst else lst[0] + list_sum(lst[1:])

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum of list:", list_sum(numbers))
