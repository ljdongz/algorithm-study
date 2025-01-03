
graph = {
  'A': ['B', 'D', 'E'],
  'B': ['A', 'C', 'D'],
  'C': ['B'],
  'D': ['A', 'B'],
  'E': ['A']
}

visited = []

def dfs(cur_v):
  visited.append(cur_v) # 현재 노드를 방문한 노드 리스트에 추가
  for v in graph[cur_v]: # 현재 노드와 연결된 모든 노드들을 반복문으로 순차 접근
    if v not in visited: # 방문한 노드가 아닌 경우
      dfs(v)


dfs('A') # Start Node = A