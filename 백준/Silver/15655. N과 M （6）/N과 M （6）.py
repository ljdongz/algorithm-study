
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

result = []

def backtrack(start, curr):
    if len(curr) == M:
        result.append(curr[:])
        return
    
    for i in range(start, N):
        curr.append(nums[i])
        backtrack(i+1, curr)
        curr.pop()

backtrack(0, [])

for r in result:
    for c in r:
        print(c, end=" ")
    print()