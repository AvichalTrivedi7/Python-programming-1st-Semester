def sum(list1):
    if list1==[]:
        return 0
    else:
        return list1.pop()+sum(list1)

print(sum([1,2,3]))

# OR

def sum(lst):
    if not lst:
        return 0
    else:
        return lst[0]+sum(lst[1:])
print(sum([1,2,3]))
