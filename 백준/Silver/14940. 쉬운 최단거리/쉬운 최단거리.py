import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque()

start = ()

for row in range(n):
  for col in range(m):
    if graph[row][col] == 2:
      start = (row, col)
      dist[row][col] = 0
      visited[row][col] = True
      q.append((row, col))
    elif graph[row][col] == 0:
      dist[row][col] = 0

while q:
  row, col = q.popleft()

  for r, c in direction:
    next_row = row + r
    next_col = col + c

    # 그래프 범위 안에 있는지 확인
    if next_row >= 0 and next_row < n and next_col >= 0 and next_col < m:
      # 다음 위치가 방문하지 않은 곳인 경우
      if not visited[next_row][next_col]:
        # 갈 수 있는 땅인 경우
        if graph[next_row][next_col] == 1:
          visited[next_row][next_col] = True
          dist[next_row][next_col] = dist[row][col] + 1
          q.append((next_row, next_col))
        else:
          visited[next_row][next_col] = True

for row in range(n):
  for col in range(m):
    print(dist[row][col], end=" ")
  print("")