# Hash Table 이용
def longestConsecutive(nums):
  longest = 0

  num_dict = set(nums)

  for num in num_dict:
    if num - 1 not in num_dict: # 연속된 수의 가장 첫 시작점인 경우
      cnt = 1
      target = num + 1
      while target in num_dict:
        target += 1
        cnt += 1
      longest = max(longest, cnt)
  return longest

# Hash Table 사용 X
def sequenceNumber(nums):
  result = 0
  count = 0
  prevNum = 0
  nums.sort()
  for idx, num in enumerate(nums):
    
    if idx == 0: 
      prevNum = num
      count += 1
      continue

    if num - prevNum == 1:
      count += 1
    elif num == prevNum:
      continue
    elif num - prevNum != 1 and result < count:
      result = count
      count = 0
    

    prevNum = num

  return max(result, count)


print(sequenceNumber([0,1,1,2,3, 5,6,7,8]))
