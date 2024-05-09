import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

while True:

    m, n = list(map(int, input().split()))

    if m == n == 0:
        break

    houses = defaultdict(list)
    visited = [False] * m

    result = 0

    for _ in range(n):
        x, y, z = list(map(int, input().split()))
        houses[x].append((y, z))
        houses[y].append((x, z))
        result += z

    hq = []
    heapq.heappush(hq, (0, 0)) # 비용, 도착지

    while hq:
        cur_cost, cur_house = heapq.heappop(hq)

        if visited[cur_house]:
            continue

        visited[cur_house] = True
        result -= cur_cost

        for next_house, next_cost in houses[cur_house]:
            if next_cost != -1 and not visited[next_house]:
                heapq.heappush(hq, (next_cost, next_house))

    print(result)
