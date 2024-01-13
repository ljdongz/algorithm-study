from collections import deque
import sys

# H: 높이, N: 행, M: 열
M, N, H = list(map(int, sys.stdin.readline().split()))

graph = []

for h in range(H):
    row = []
    for n in range(N):
        row.append(list(map(int, input().split())))
    graph.append(row)

q = deque()
count = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                q.append((h, n, m, 0))

dhdndm = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

while q:
    cur_h, cur_n, cur_m, cur_count = q.popleft()
    count = max(count, cur_count)
    for h, n, m in dhdndm:
        next_h = cur_h + h
        next_n = cur_n + n
        next_m = cur_m + m
        if next_h >= 0 and next_h < H and next_n >= 0 and next_n < N and next_m >= 0 and next_m < M:
            if graph[next_h][next_n][next_m] == 0:
                graph[next_h][next_n][next_m] = 1
                q.append((next_h, next_n, next_m, cur_count + 1))

def isValid():
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m] == 0:
                    return False

    return True

if isValid():
    print(count)
else:
    print(-1)