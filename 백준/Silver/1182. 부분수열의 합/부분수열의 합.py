
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

nums = list(map(int, input().split()))

result = 0

def backtrack(start, curr, sum):
    global result
    if len(curr) == k:
        if sum == M:
            result += 1
        return
        
    for i in range(start, N):
        curr.append(nums[i])
        backtrack(i+1, curr, sum + nums[i])
        curr.pop()

for k in range(1, N+1):
    backtrack(0, [], 0)

print(result)