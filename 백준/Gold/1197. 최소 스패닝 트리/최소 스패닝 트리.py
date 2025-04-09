import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

V, E = list(map(int, input().split()))

parents = [i for i in range(V+1)]
graph = []
result = 0

for _ in range(E):
  v1, v2, w = list(map(int, input().split()))
  graph.append((w, (v1, v2)))
graph.sort()

def find_parent(x):
  if parents[x] != x:
    parents[x] = find_parent(parents[x])
  return parents[x]

def union(x, y):
  xNode = find_parent(x)
  yNode = find_parent(y)
  parents[xNode] = yNode

for weight, (v1, v2) in graph:
  rootX = find_parent(v1)
  rootY = find_parent(v2)
  if rootX != rootY:
    result += weight
    union(v1, v2)

print(result)