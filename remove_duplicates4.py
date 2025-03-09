#nums = [1,1,1,1,1]
#nums = [1,1,2]
nums =[0,0,1,1,1,2,2,3,3,4]


length = len(nums)
new_nums = []

for i in range(length):
    if nums[i] not in new_nums:
       new_nums.append(nums[i])

nums = new_nums
print(nums)