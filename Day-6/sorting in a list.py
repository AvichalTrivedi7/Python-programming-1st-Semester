list1=[1,5,7,2,4,10]
for i in range(0,len(list1)):
    for j in range(0,len(list1)-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print("This is the sorted list: ",list1)