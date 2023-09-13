def twoSum(nums, target):
  dict = {}
  for num in nums:
    value = target - num
    if value in dict:
      return True
    dict[num] = True
    
  return False

print(twoSum({4,1,9,7,5,3,16}, 14))
print(twoSum({2, 1, 5, 7}, 4))