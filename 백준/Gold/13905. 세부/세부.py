import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = list(map(int, input().split()))

start, end = list(map(int, input().split()))

bridges = defaultdict(list)
for _ in range(M):
    h1, h2, k = list(map(int, input().split()))
    bridges[h1].append((h2, k))
    bridges[h2].append((h1, k))

visited = [False] * (N+1)
visited[start] = True

result = 1000001

hq = []
for island, weight in bridges[start]:
    heapq.heappush(hq, (-weight, island, result)) # 무개, 다음 섬, 최소 무게



while hq:
    cur_bridge_weight, cur_island, min_weight = heapq.heappop(hq)

    if cur_island == end:
        result = min(min_weight, -cur_bridge_weight)
        break
    
    if visited[cur_island]:
        continue

    visited[cur_island] = True

    for next_island, next_bridge_weight in bridges[cur_island]:
        if not visited[next_island]:
            heapq.heappush(hq, (-next_bridge_weight, next_island, min(min_weight, -cur_bridge_weight)))

if result != 1000001:
    print(result)
else:
    print(0)