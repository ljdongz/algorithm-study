def solution(s: str):
  sp = s.split(sep=" ")
  nums = []
  
  for i in sp:
    nums.append(int(i))

  maximum = max(nums)
  minimum = min(nums)

  return f"{minimum} {maximum}"

print(solution("1 2 3 4"))