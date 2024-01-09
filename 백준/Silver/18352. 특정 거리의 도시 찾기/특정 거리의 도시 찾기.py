from collections import defaultdict
import heapq, sys

"""
N: 도시의 개수
M: 도로의 개수
K: 거리 정보
X: 출발 도시 번호
"""

N, M, K, X = list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
for _ in range(M):
    start, end = list(map(int, sys.stdin.readline().split()))
    graph[start].append(end)

def dijkstra():
    costs = {}
    pq = []
    cities = []

    heapq.heappush(pq, (0, X)) # 방문할 도시까지의 총 가중치, 방문할 도시

    while pq:
        cur_cost, cur_city = heapq.heappop(pq)
        if cur_city not in costs:
            costs[cur_city] = cur_cost
            if cur_cost == K:
                cities.append(cur_city)
            else:
                for next_city in graph[cur_city]:
                    heapq.heappush(pq, (cur_cost + 1, next_city))

    if cities:
        cities.sort()
        for city in cities:
            print(city)
    else:
        print(-1)

dijkstra()
