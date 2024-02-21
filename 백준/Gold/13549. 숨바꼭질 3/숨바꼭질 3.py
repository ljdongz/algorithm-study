
from collections import deque
import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

visited = [False] * 100001

q = deque()
q.append((0, N)) # 걸린 시간, 현재 위치
visited[N] = True

while q:
    cur_time, cur_dot = q.popleft()

    if cur_dot == K:
        print(cur_time)
        break

    """
    1. 순간이동(*2)는 시간이 소요되지 않기 때문에 우선 순위로 둔다.
    2. 순간이동을 효율적으로 활용하기 위해 -1을 +1보다 우선순위로 둔다.
        ex) 4 -> 6인 경우.
        4 -> 5 -> 6 = 2
        4 -> 3 -> 6 = 1
    """
    next = [(cur_time, cur_dot * 2), (cur_time + 1, cur_dot - 1), (cur_time + 1, cur_dot + 1)]
    for next_time, next_dot in next:
        if next_dot >= 0 and next_dot <= 100000 and not visited[next_dot]:
            visited[next_dot] = True
            q.append((next_time, next_dot))
