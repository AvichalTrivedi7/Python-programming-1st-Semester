set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))

print("Is Set1 a subset of Set2?", set1.issubset(set2))
print("Is Set1 a superset of Set2?", set1.issuperset(set2))
