import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
removeTarget = int(input())

dict = defaultdict(list)
root = 0

for vertex in range(len(parents)):
  parent = parents[vertex]
  if parent == -1:
    root = vertex
  dict[parent].append(vertex)

def dfs(v):
  if v == removeTarget:
    return 0
  
  child = dict[v]

  if len(child) == 0:
    return 1
  
  result = 0
  for i in range(len(child)):
    result += dfs(child[i])
  
  if result == 0:
    result += 1

  return result
  
if len(dict[root]) == 0:
  print(0)
else:
  print(dfs(root))