

import sys
input = sys.stdin.readline


N, M = list(map(int, input().split()))

gender = [""] + list(map(str, input().split()))

route = []
for _ in range(M):
    u, v, d = list(map(int, input().split()))
    route.append((d, (u, v)))
route.sort()

parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    rootX = find_parent(x)
    rootY = find_parent(y)
    parent[rootY] = rootX

def kruskal():
    result = 0

    for d, (u, v) in route:
        if gender[u] == gender[v]:
            continue

        if find_parent(u) != find_parent(v):
            result += d
            union(u, v)

    root = find_parent(parent[1])
    for i in range(2, len(parent)):
        if root != find_parent(parent[i]):
            print(-1)
            return

    print(result)

kruskal()