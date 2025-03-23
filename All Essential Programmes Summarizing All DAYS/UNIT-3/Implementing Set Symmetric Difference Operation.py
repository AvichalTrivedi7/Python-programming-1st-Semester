set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of sets:", symmetric_difference_set)
