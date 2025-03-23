nums=eval(input("Enter the list: "))


target=int(input("Enter the sum you require from the elements of the list: "))


for i in range(len(nums)):


    for j in range(len(nums)):


        if nums[i]+nums[j]==target:


            a=i


            b=j
            
            break
        
if a<b:
    print([a,b])
else:
    print([b,a])


#***Leetcode accepted solution***

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    a=i
                    b=j
                    break
        if a<b:
            return [a,b]
        else:
            return [b,a]
        




