
import sys, heapq

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(0)
else:
    pq = [(0,0)] # (cost, cur_node)
    visited = [False] * N
    result = 0

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if not visited[cur_node]:
            result += cur_cost
            visited[cur_node] = True

            for next_node, next_cost in enumerate(graph[cur_node]):
                if cur_node != next_node:
                    heapq.heappush(pq, (next_cost, next_node))

    print(result)