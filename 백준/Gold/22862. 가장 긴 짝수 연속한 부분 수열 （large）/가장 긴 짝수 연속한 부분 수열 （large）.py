import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))
nums = list(map(int, input().split()))

start = end = 0
result = 0
cur_length = 0
cnt = 0

while end < N:
    if cnt <= K:
        if nums[end] % 2 == 0:
            cur_length += 1
            result = max(result, cur_length)
        else:
            cnt += 1
        end += 1 
    else:
        if nums[start] % 2 == 0:
            cur_length -= 1
        else:
            cnt -= 1
        start += 1

print(result)