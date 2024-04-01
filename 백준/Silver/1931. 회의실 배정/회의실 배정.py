import sys

input = sys.stdin.readline

N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]

meetings = sorted(meetings, key=lambda x : (x[1], x[0]))

cur = [0, 0]

result = 0

for meeting in meetings:
    if cur[1] <= meeting[0]:
        result += 1
        cur = meeting

print(result)