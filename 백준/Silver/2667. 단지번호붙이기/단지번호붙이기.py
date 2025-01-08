import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

visited = [[True] * N for _ in range(N)]
graph = [[0] * N for _ in range(N)]

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for row in range(N):
  string = input().rstrip()
  col = 0
  for s in string:
    if s == "1":
      visited[row][col] = False
      graph[row][col] = 1
    col += 1

houseCount = []

for row in range(N):
  for col in range(N):
    if visited[row][col]:
      continue
    
    count = 1
    q = deque()
    q.append((row, col))
    visited[row][col] = True

    while q:
      cur_row, cur_col = q.popleft()

      for r, c in dir:
        next_row = cur_row + r
        next_col = cur_col + c

        if next_row >= 0 and next_row < N and next_col >= 0 and next_col < N:
          if not visited[next_row][next_col]:
            visited[next_row][next_col] = True
            q.append((next_row, next_col))
            count += 1

    houseCount.append(count)

houseCount.sort()
print(len(houseCount))
for c in houseCount:
  print(c)