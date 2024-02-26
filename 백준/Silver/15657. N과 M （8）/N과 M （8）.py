
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
    
    for i in range(start, len(nums)):
        curr.append(nums[i])
        backtrack(i, curr)
        curr.pop()

backtrack(0, [])

for res in result:
    for r in res:
        print(r, end=" ")
    print()