# Your code here
nums = [(1, 3), (5, 8), (4, 10), (20, 25), (24,30), (1,3), (2,4), (3,5)]
nums = sorted(nums, key= lambda x: x[0])

i = 0
kt = False
try:
  while i < len(nums):
    while nums[i][1] > nums[i+1][0]:
      if nums[i][1] > nums[i+1][1]:
        nums.remove(nums[i+1])
      else:
        nums.insert(0,(nums[i][0],nums[i+1][1]))
        nums.remove(nums[i+1])
        nums.remove(nums[i+1])
    i += 1
except IndexError:
  pass

print(sorted(nums))