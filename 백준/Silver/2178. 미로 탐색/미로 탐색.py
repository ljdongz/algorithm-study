from collections import deque

row, col = map(int, input().split())

graph = []

for _ in range(row):
    string = input()
    column = []
    for s in string:
        column.append(int(s))
    graph.append(column)

def bfs():
    graph[0][0] = -1 # -1: 방문한 위치
    q = deque()
    q.append((0, 0, 1))

    drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        cur_row, cur_col, cur_count = q.popleft()

        if cur_row == row - 1 and cur_col == col - 1:
            return cur_count

        for r, c in drdc:
            next_row = cur_row + r
            next_col = cur_col + c
            if next_row >= 0 and next_row < row and next_col >= 0 and next_col < col:
                if graph[next_row][next_col] == 1:
                    graph[next_row][next_col] = -1
                    q.append((next_row, next_col, cur_count + 1))

print(bfs())
