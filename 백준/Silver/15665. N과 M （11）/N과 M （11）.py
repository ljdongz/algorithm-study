
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

nums = list(map(int, input().split()))
nums.sort()

result = []
memo = {}

def backtrack(curr):
    if len(curr) == M:
        if tuple(curr) not in memo:
            result.append(curr[:])
            memo[tuple(curr)] = True
        return
    
    for i in range(len(nums)):
        curr.append(nums[i])
        backtrack(curr)
        curr.pop()
        

backtrack([])

for res in result:
    for r in res:
        print(r, end=" ")
    print()


