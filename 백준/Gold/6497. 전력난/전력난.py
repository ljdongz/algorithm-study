import sys
import heapq
from collections import defaultdict

sys.setrecursionlimit(100000)

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    rootX = find_parent(parent, x)
    rootY = find_parent(parent, y)
    parent[rootX] = rootY

while True:
    m, n = list(map(int, input().split()))

    if m == n == 0:
        break

    result = 0

    parent = [i for i in range(m)]

    cities = []
    for _ in range(n):
        x, y, cost = list(map(int, input().split()))
        cities.append((cost, x, y))
        result += cost
    cities.sort()

    for cost, x, y in cities:
        rootX = find_parent(parent, x)
        rootY = find_parent(parent, y)

        if rootX != rootY:
            result -= cost
            union_parent(parent, rootX, rootY)

    print(result)