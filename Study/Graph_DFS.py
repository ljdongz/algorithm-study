
graph = {
  'A': ['B', 'D', 'E'],
  'B': ['A', 'C', 'D'],
  'C': ['B'],
  'D': ['A', 'B'],
  'E': ['A']
}

visited = []

def dfs(cur_v):
  visited.append(cur_v)
  for v in graph[cur_v]:
    if v not in visited: # 이미 방문한 노드인지 확인
      dfs(v)


dfs('A') # Start Node = A