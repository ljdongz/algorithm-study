from collections import deque

"""
Tree와는 달리 Graph에서는 Queue에서 pop한 노드를 visited에 추가하지 않음.
즉, 다음에 방문할 노드를 visited에 미리 추가해놓음.
그 이유로는, Tree는 탐색 방향이 한 방향. (Root를 시작으로 부모 노드에서 자식 노드로)
하지만, Graph는 탐색 방향이 여러 방향임.
즉, 다음에 방문할 노드를 visited에 미리 추가하면서 중복 방문을 예방.
"""

def bfs(graph, start_v):
  visited = [start_v] # 방문한 노드 리스트
  queue = deque(start_v) # 방문할 노드 리스트
  
  while queue:
    cur_v = queue.popleft()
    for v in graph[cur_v]: # 현재 노드에 연결된 모든 노드들
      if v not in visited: # 이미 방문한 노드인지 확인
        visited.append(v) # 방문할 노드를 미리 추가 (중복 방문 방지)
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