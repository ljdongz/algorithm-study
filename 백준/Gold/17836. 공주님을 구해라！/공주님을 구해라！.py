
from collections import deque
import sys

input = sys.stdin.readline

N, M, T = list(map(int, input().split()))

# 0: 빈 공간, 1: 벽, 2: 검
graph = [list(map(int, input().split())) for _ in range(N)]
graph[0][0] = -1

visited = [[False] * M for _ in range(N)]

drdc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque()
q.append((0, (0, 0))) # 걸린 시간, 현재 위치

result = "Fail"
total_time = T + 1

while q:
    cur_time, (cur_row, cur_col) = q.popleft()

    if (cur_row, cur_col) == (N-1, M-1):
        total_time = min(cur_time, total_time)
        break

    if cur_time >= T:
        continue

    for r, c in drdc:
        next_row = cur_row + r
        next_col = cur_col + c

        # 다음 칸이 정해진 범위 내에 있는 경우
        if next_row >= 0 and next_row < N and next_col >= 0 and next_col < M:
            
            if graph[next_row][next_col] != 1 and not visited[next_row][next_col]:
                # 다음 칸이 검이 있는 칸인 경우 검 소유 여부 업데이트
                if graph[next_row][next_col] == 2:
                    time = ((N-1) - next_row) + ((M-1) - next_col) + 1
                    total_time = min(total_time, cur_time + time)
                    visited[next_row][next_col] = True
                else:
                    visited[next_row][next_col] = True
                    q.append((cur_time + 1, (next_row, next_col)))
                
if total_time > T:
    print("Fail")
else:
    print(total_time)   