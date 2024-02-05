import sys

input = sys.stdin.readline

N = int(input())

array = []

for i in range(N):
    x, r = list(map(int, input().split()))
    array.append((x-r, i))
    array.append((x+r, i))

array.sort()

stack = []

for x, i in array:
    if not stack:
        stack.append((x, i))
    else:   
        if stack[-1][1] != i:
            stack.append((x, i))
        else:
            stack.pop()

if stack:
    print("NO")
else:
    print("YES")
    