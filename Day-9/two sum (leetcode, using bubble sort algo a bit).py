nums=eval(input("Enter the list: "))

target=int(input("Enter the sum you require from the elements of the list: "))

for i in range(len(nums)):

    for j in range(len(nums)-1):

        if nums[j]+nums[j+1]==target:

            a=j

            b=j+1

print("The indices are: ",[a,b])




'''YOOOOO i did it, i used the algorithm i remembered for bubble sort using
 nested loop.... 
in which you 
trace through the entire list while sorting it in real time, two 
elements at once and so on'''