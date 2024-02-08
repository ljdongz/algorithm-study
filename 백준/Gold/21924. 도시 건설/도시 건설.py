

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find_parent(parent, x)
    rootY = find_parent(parent, y)
    parent[rootY] = rootX

def kruskal(total_cost):
    parent = [i for i in range(N+1)]

    for cost, (nodeX, nodeY) in graph:
        rootX = find_parent(parent, nodeX)
        rootY = find_parent(parent, nodeY)

        if rootX != rootY:
            union(parent, nodeX, nodeY)
            total_cost -= cost

    rootParent = find_parent(parent, 1)
    for i in range(2, N+1):
        if rootParent != find_parent(parent, i):
            total_cost = -1
            break
    print(total_cost)

N, M = list(map(int, input().split()))

total_cost = 0
graph = []
for _ in range(M):
    nodeX, nodeY, cost = list(map(int, input().split()))
    graph.append((cost, (nodeX, nodeY)))
    total_cost += cost
graph.sort()


kruskal(total_cost)