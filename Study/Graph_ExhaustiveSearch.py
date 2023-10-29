from collections import deque

def numIslandBFS(grid):
  number_of_island = 0

  row = len(grid)
  col = len(grid[0])
  visited = [[False]*col for _ in range(row)] # 방문 한 노드들 위치를 표시하기 위한 리스트 선언

  def bfs(x, y):
    # dx, dy를 이용하여 상하좌우 이동 
    # (ex. dx[0] + dy[0] == '좌'로 한 칸 이동)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True # 방문한 노드 (현재 위치를 방문했음을 표시)
    queue = deque() # 방문할 노드
    queue.append((x, y))

    while queue:
      cur_x, cur_y = queue.popleft()
      for i in range(4): # 왼(-1, 0), 오(1, 0), 하(0, -1), 상(0, 1) 순으로 접근
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        # grid 범위를 넘지 않은 인덱스인 경우
        if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
          # 방문할 노드가 "1"(땅) 이면서, 이미 방문한 노드가 아닌 경우
          if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            queue.append((next_x, next_y))

  # grid내 각 노드들을 순차적으로 접근
  for i in range(row):
    for j in range(col):
      if grid[i][j] == "1" and not visited[i][j]:
        bfs(i, j) # 너비 우선 탐색으로 island를 찾음
        number_of_island += 1 # 하나의 island를 찾은 후 1 증가

  return number_of_island


# 암시적 그래프 (2차원 배열로 표현)

grid = [
  ['1', '1', '1', '1', '0'],
  ['1', '1', '0', '1', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '0', '0', '0']
]

grid2 = [
  ['1', '1', '0', '0', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '1', '0', '0'],
  ['0', '0', '0', '1', '1']
]

print(numIslandBFS(grid))