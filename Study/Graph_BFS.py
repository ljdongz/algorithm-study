from collections import deque

"""
Tree와는 달리 Graph에서는 Queue에서 pop한 노드를 visited에 추가하지 않음.
즉, 다음에 방문할 노드를 visited에 미리 추가해놓음.
그 이유로는, Tree에서는 특정 노드까지 갈 수 있는 경로가 하나뿐임. (수직적)
하지만, Graph는 특정 노드까지 갈 수 있는 경로가 여러개가 될 수 있음. (수평적)
즉, 다음에 방문할 노드를 visited에 미리 추가하지 않으면 다른 노드에서 해당 노드에 방문할 수 있어 중복 발생.
"""

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

print(bfs(graph, 'A'))