import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = list(map(int, input().split()))

visited = [False] * (V + 1)
graph = defaultdict(list)

for _ in range(E):
  v1, v2, w = list(map(int, input().split()))
  graph[v1].append((v2, w))
  graph[v2].append((v1, w))

hq = []
heapq.heappush(hq, (0, 1))

result = 0

while hq:
  cur_weight, cur_node = heapq.heappop(hq)

  if not visited[cur_node]:
    result += cur_weight
    visited[cur_node] = True

    for (next_node, next_weight) in graph[cur_node]:
      if not visited[next_node]:
        heapq.heappush(hq, (next_weight, next_node))

print(result)