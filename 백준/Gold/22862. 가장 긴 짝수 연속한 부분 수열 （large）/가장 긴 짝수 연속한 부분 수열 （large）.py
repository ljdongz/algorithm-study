import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))
nums = list(map(int, input().split()))

start, end = 0, 0

k_count = 0
length = 0
result = 0

while end < N:
  if k_count <= K:
    if nums[end] % 2 == 1:
      k_count += 1
    else:
      length += 1
      result = max(result, length)
    end += 1

  else:
    if nums[start] % 2 == 1:
      k_count -= 1
    else:
      length -= 1
    start += 1

print(result)