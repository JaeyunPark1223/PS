nums = list(map(int,input().split()))

nums.sort()
print(nums[0],nums[1],(nums[-1]-nums[0]-nums[1]))
