from collections import defaultdict
import sys, heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)
visited = [False] * N
result = 0
pq = []

for _ in range(M):
    start, end, cost = list(map(int, input().split()))
    graph[start].append((cost, end))
    graph[end].append((cost, start))

heapq.heappush(pq, (0, 1))

while pq:
    
    cur_cost, cur_com = heapq.heappop(pq)
    if not visited[cur_com - 1]:
        result += cur_cost
        visited[cur_com - 1] = True
        

        for next_cost, next_com in graph[cur_com]:
            heapq.heappush(pq, (next_cost, next_com))

print(result)