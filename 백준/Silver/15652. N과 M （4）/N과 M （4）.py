
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

result = []

def backtrack(start, curr):
    if len(curr) == M:
        result.append(curr[:])
        return
    
    for i in range(start, N+1):
        curr.append(i)
        backtrack(i, curr)
        curr.pop()

backtrack(1, [])

for r in result:
    for c in r:
        print(c, end=" ")
    print()