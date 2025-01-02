import sys

input = sys.stdin.readline

string = list(input().rstrip())

target = list(input().rstrip())

stack = []
for s in string:
    stack.append(s)

    if len(stack) < len(target):
        continue

    if stack[-len(target):] == target:
        for _ in range(len(target)):
            stack.pop()

print("".join(stack) if stack else "FRULA")
