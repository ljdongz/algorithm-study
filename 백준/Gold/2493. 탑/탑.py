import sys
input = sys.stdin.readline

N = int(input())

tops = list(map(int, input().split()))

stack = []
receive = [0] * N

for idx, height in enumerate(tops):
    
    while stack and stack[-1][1] <= height:
        stack.pop()

    if stack:
        receive[idx] = stack[-1][0] + 1

    stack.append((idx, height))

for i in range(N):
    print(receive[i], end=" ")