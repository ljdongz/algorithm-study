
# def twoSum(nums, target):
#   dict = {}
#   for num in nums:
#     value = target - num
#     if value in dict:
#       return True
#     dict[num] = True
    
#   return False

def two_sum(nums, target):
  memo = {}
  for v in nums:
    memo[v] = 1

  for v in nums:
    needed_number = target - v
    if needed_number in memo:
      return True
    
  return False

print(two_sum({4,1,7,5,3,16}, 14))


# print(twoSum({4,1,9,7,5,3,16}, 14))
# print(twoSum({2, 1, 5, 7}, 4))