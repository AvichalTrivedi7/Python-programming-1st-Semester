set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)
