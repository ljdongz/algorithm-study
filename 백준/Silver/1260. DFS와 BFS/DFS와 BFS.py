import sys
from collections import deque

input = sys.stdin.readline

N, M, V = list(map(int, input().split()))

graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    r, c = list(map(int, input().split()))
    graph[r][c] = True
    graph[c][r] = True


def dfs():
    visited = [False] * (N+1)
    result = []

    def recursive(cur_node):

        visited[cur_node] = True
        result.append(cur_node)
        
        for next_node, isConnected in enumerate(graph[cur_node]):
            if isConnected and not visited[next_node]:
                recursive(next_node)


    recursive(V)
    
    for r in result:
        print(r, end=" ")


def bfs():
    result = [V]
    visited = [False] * (N+1)
    visited[V] = True

    q = deque()
    q.append(V)

    while q:
        cur_node = q.popleft()

        for next_node, isConnected in enumerate(graph[cur_node]):
            if isConnected and not visited[next_node]:
                result.append(next_node)
                q.append(next_node)
                visited[next_node] = True
    
    for r in result:
        print(r, end=" ")



dfs()
print()
bfs()