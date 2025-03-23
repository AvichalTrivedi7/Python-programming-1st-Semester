set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))
union_set = set1.union(set2)
print("Union of sets:", union_set)
