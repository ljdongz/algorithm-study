import sys

input = sys.stdin.readline

N, S = list(map(int, input().split()))

nums = list(map(int, input().split()))

start = end = 0
cur_sum = 0
result = 100000

while end < N:
    if cur_sum < S:
        cur_sum += nums[end]
        end += 1
    else:
        result = min(result, end - start)
        cur_sum -= nums[start]
        start += 1

if cur_sum >= S:
    while cur_sum >= S:
        result = min(result, end - start)
        cur_sum -= nums[start]
        start += 1
    print(result)
elif start != 0:
    print(result)
else:
    print(0)
    