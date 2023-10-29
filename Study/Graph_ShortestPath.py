from collections import deque

def shortestPathBinaryMatrix(grid):
  shortest_path_len = -1
  row = len(grid) # n x n 크기
  col = len(grid[0])

  if grid[0][0] != 0 or grid[row-1][col-1] != 0:
    return shortest_path_len

  visited = [[False]*col for _ in range(row)]
  queue = deque()
  queue.append((0, 0, 1)) # row, col, 현재까지 길이
  visited[0][0] = True

  delta = [(1,0), (-1,0), (0,1), (0,-1),
           (1,1), (1,-1), (-1,-1), (-1,1)]

  while queue:
    cur_row, cur_col, cur_len = queue.popleft()

    # 목적지에 도착했을 때
    if cur_row == row - 1 and cur_col == col - 1:
      shortest_path_len = cur_len
      break

    for dr, dc in delta:
      next_row = cur_row + dr
      next_col = cur_col + dc
      if next_row >= 0 and next_row < row and next_col >= 0 and next_col < col:
        if grid[next_row][next_col] == 0 and not visited[next_row][next_col]:
          visited[next_row][next_col] = False
          queue.append((next_row, next_col, cur_len + 1))

  return shortest_path_len

grid = [
  [0, 1, 1, 1, 0],
  [0, 0, 0, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0]
]

print(shortestPathBinaryMatrix(grid))