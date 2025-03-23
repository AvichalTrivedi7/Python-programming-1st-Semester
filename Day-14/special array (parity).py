x=True
for i in range(len(nums)-1):
    if nums[i]%2==0 and nums[i+1]%2==0 or nums[i]%2!=0 and nums[i+1]%2!=0: 
        x=False
    else:
        pass
print(x)


# ***ANOTHER WAY***

x=True
for i in range(len(nums)-1):
    if nums[i+1]%2==nums[i]%2:
        return False
    return x 