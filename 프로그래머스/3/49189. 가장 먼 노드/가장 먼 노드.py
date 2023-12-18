from collections import deque

def solution(n, vertex: list):
    answer = 0
    result = [0 for _ in range(n)]
    
    visited = [False for _ in range(n)]
    visited[0] = True
    q = deque()
    q.append((1, 0))

    graph = {}

    for e1, e2 in vertex:
        if e1 not in graph:
            graph[e1] = []
        if e2 not in graph:
            graph[e2] = []

        graph[e1].append(e2)
        graph[e2].append(e1)


    while q:
        cur_edge, count = q.popleft()

        for edge in graph[cur_edge]:
            if not visited[edge-1]:
                visited[edge-1] = True
                q.append((edge, count + 1))
            else:
                result[cur_edge-1] = count

    answer = result.count(max(result))

    return answer