def solution(n):
  result = 0
  
  sum = 0
  for i in range(1, n + 1):
    for j in range(i, n + 1):
      sum += j

      if sum == n:
        result += 1
        sum = 0
        break

      if sum > n:
        sum = 0
        break

    sum = 0
  return result