import heapq
from collections import defaultdict

def network_delay_time(times: list, n, k):

    costs = {}
    pq = []

    # Case 1. 기본 dict 사용
    graph = {}
    for time in times:
        graph[time[0]] = graph.get(time[0], []) + [(time[2], time[1])]

    # Case 2. defaultdict 사용
    dgraph = defaultdict(list)
    for time in times:
        dgraph[time[0]].append((time[2], time[1]))

    heapq.heappush(pq, (0, k))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            if cur_v not in graph:
                continue
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))

    if len(costs) == n:
        return max(costs.values())
    else:
        return -1

print(network_delay_time([[2,1,2], [2,3,5], [2,4,1], [4,3,3]], 4, 2))
