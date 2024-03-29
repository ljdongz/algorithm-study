
"""
두 노드 사이의 최단 거리를 구하는 알고리즘

<<< 구현 방법 >>>
1. 우선순위 큐에 시작 노드 추가
  (2 ~ 5: 우선순위 큐에 노드가가 존재할 때 까지 반복)
  2. 우선순위가 가장 높은 노드 추출 (비용이 가장 낮은)
  3. 방문 여부 확인 (이미 방문한 노드인 경우 4 ~ 5 pass)
    4. 비용 업데이트
    5. 현재 노드와 연결된 노드들을 우선순위 큐에 추가
6. 목적지에 기록된 비용 반환
"""

import heapq

def dijkstra(graph, start, final):
    costs = {} # 노드에 대한 비용
    pq = [] # 방문할 노드 정보 (방문할 노드까지의 비용, 방문할 노드, 방문할 노드까지의 경로)

    heapq.heappush(pq, (0, start, [start])) # 1. 우선순위 큐에 시작 노드 추가

    while pq:
        cur_cost, cur_v, cur_route = heapq.heappop(pq) # 2. 우선순위가 가장 높은 노드 추출
        if cur_v not in costs: # 3. 방문 여부 확인
            costs[cur_v] = (cur_cost, cur_route) # 4. 비용 업데이트
            for cost, next_v in graph[cur_v]: # 5. 현재 노드와 연결된 노드들을 우선순위 큐에 추가
                next_cost = cur_cost + cost 
                next_route = cur_route + [next_v]
                heapq.heappush(pq, (next_cost, next_v, next_route))
    
    return costs[final] # 6. 목적지에 기록된 비용 반환

# (비용, 노드)
# graph = {
#     1: [(2, 2), (1, 4)],
#     2: [(1, 3), (9, 5), (6, 6)],
#     3: [(4, 6)],
#     4: [(3, 3), (5, 7)],
#     5: [(1, 8)],
#     6: [(3, 5)],
#     7: [(7, 6), (9, 8)],
#     8: []
# }

graph = {
    1: [(2,2), (1,4), (2,3)],
    2: [(2,4), (3,3)],
    3: [(1,5), (5,6), (3,4)],
    4: [(1,5)],
    5: [(2,6)],
    6: []
}

print(dijkstra(graph, 1, 6))
