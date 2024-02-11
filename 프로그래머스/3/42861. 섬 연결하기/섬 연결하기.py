from collections import defaultdict
import heapq

def solution(n, costs):
    answer = 0

    graph = defaultdict(list)
    for x, y, cost in costs:
        graph[x].append((cost, y))
        graph[y].append((cost, x))
    visited = [False] * n

    pq = [(0,0)] # 비용, 노드

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if not visited[cur_node]:
            answer += cur_cost
            visited[cur_node] = True

            for next_cost, next_node in graph[cur_node]:
                heapq.heappush(pq, (next_cost, next_node))


    return answer
