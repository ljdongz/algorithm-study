
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
        if num not in curr:
            curr.append(num)
            backtrack(curr)
            curr.pop()

backtrack([])

for r in result:
    for c in r:
        print(c, end=" ")
    print()