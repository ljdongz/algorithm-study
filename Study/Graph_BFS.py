from collections import deque

def bfs(graph, start_v):
  visited = [start_v]
  queue = deque(start_v)

  while queue:
    cur_v = queue.popleft()
    for v in graph[cur_v]:
      if v not in visited: # 이미 방문한 노드인지 확인
        visited.append(v)
        queue.append(v)
    
  return visited

graph = {
  'A': ['B', 'D', 'E'],
  'B': ['A', 'C', 'D'],
  'C': ['B'],
  'D': ['A', 'B'],
  'E': ['A']
}