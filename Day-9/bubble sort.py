list1=eval(input("Enter the list: "))
for i in range(len(list1)):
	for j in range(0,len(list1)-1):
		if list1[j]>list1[j+1]:
		    list1[j],list1[j+1]=list1[j+1],list1[j]
print(" smallest: ",list1[0],"\n","biggest: ",list1[-1])
