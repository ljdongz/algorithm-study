from collections import deque

def bfs(graph, start_v):
  visited = [start_v] # 방문한 노드 리스트
  queue = deque(start_v) # 방문할 노드 리스트

  while queue:
    cur_v = queue.popleft()
    for v in graph[cur_v]: # 현재 노드에 연결된 모든 노드들
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