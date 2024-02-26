
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

nums = list(map(int, input().split()))
nums.sort()

result = []

def backtrack(curr):
    if len(curr) == M:
        result.append(curr[:])
        return 
    
    for num in nums:
        curr.append(num)
        backtrack(curr)
        curr.pop()

backtrack([])

for res in result:
    for r in res:
        print(r, end=" ")
    print()