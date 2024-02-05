import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    h = int(input())

    while stack and stack[-1] <= h:
        stack.pop()

    stack.append(h)

print(len(stack))
