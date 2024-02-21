
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

result = []

def backtrack(curr):
    if len(curr) == M:
        result.append(curr[:])
        return
    
    for i in range(1, N+1):
        if i not in curr:
            curr.append(i)
            backtrack(curr)
            curr.pop()

backtrack([])

for r in result:
    for c in r:
        print(c, end=" ")
    print()