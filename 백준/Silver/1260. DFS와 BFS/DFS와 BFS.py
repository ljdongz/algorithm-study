from collections import deque, defaultdict

vertexes, edges, startV = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(edges):
    start, end = list(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)

for key in graph.keys():
    graph[key].sort()

visitedBfs = []
visitedDfs = []

def bfs():
    visitedBfs = [startV]
    q = deque()
    q.append(startV)

    while q:
        cur_v = q.popleft()
        print(cur_v, end=" ")
        for next_v in graph[cur_v]:
            if next_v not in visitedBfs:
                visitedBfs.append(next_v)
                q.append(next_v)


def dfs(vertex):
    visitedDfs.append(vertex)
    print(vertex, end=" ")
    for next_v in graph[vertex]:
        if next_v not in visitedDfs:
            dfs(next_v)

dfs(startV)
print()
bfs()