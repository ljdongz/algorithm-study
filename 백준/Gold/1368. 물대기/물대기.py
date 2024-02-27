
import sys, heapq

input = sys.stdin.readline

N = int(input())

costs = [0]
for _ in range(N):
    costs.append(int(input()))

graph = [[0] * (N+1) for _ in range(N+1)]
graph[0] = costs
for i in range(1, N+1):
    graph[i] = [costs[i]] + list(map(int, input().split()))

visited = [False] * (N+1)

totalCost = 0

pq = [(0, 0)]

while pq:
    cur_cost, cur_node = heapq.heappop(pq)

    if not visited[cur_node]:
        visited[cur_node] = True

        totalCost += cur_cost

        for next_node, next_cost in enumerate(graph[cur_node]):
            heapq.heappush(pq, (next_cost, next_node))

print(totalCost)