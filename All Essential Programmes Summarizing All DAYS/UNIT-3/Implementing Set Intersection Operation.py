set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)
