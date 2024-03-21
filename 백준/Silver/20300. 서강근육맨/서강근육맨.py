import sys

input = sys.stdin.readline

N = int(input())

t = list(map(int, input().split()))

maximum = 0

t.sort()

if len(t) % 2 == 1:
    maximum = t.pop()

for i in range(int(len(t) / 2)):
    sum = t[i] + t[-(i+1)]
    if maximum < sum:
        maximum = sum

print(maximum)