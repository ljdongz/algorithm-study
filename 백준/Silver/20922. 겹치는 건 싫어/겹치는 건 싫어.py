import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

sequence = list(map(int, input().split()))

nums = [0 for i in range(100001)]

start, end = 0, 0
result = 0
cur_len = 0

while end < N:
    nums[sequence[end]] += 1

    if nums[sequence[end]] > K:

        result = max(result, cur_len)

        while nums[sequence[end]] > K:
            nums[sequence[start]] -= 1
            start += 1
            cur_len -= 1

    end += 1
    cur_len += 1

result = max(result, cur_len)
print(result)
