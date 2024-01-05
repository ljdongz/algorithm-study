import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        costs = {}
        pq = []

        graph = {}
        for time in times:
            graph[time[0]] = graph.get(time[0], []) + [(time[2], time[1])]

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