
from collections import deque

def solution(maps: list):

    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = True
    q = deque()
    q.append((0,0,1)) # row, col, 이동한 칸

    max_row = len(maps) - 1
    max_col = len(maps[0]) - 1

    if maps[0][0] == 0 or maps[max_row][max_col] == 0:
        return -1

    drdc = [(1,0),(-1,0),(0,1),(0,-1)]

    while q:
        cur_row, cur_col, cur_count = q.popleft()

        if cur_row == max_row and cur_col == max_col:
            return cur_count

        for row, col in drdc:
            next_row = cur_row + row
            next_col = cur_col + col

            if next_row >= 0 and next_row <= max_row and next_col >= 0 and next_col <= max_col:
                if maps[next_row][next_col] == 1 and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col, cur_count + 1))

    return -1