from collections import deque

# BFS(너비 우선 탐색) 기본 개념. (Level Order)
def bfs(root):

  if root is None:
    return []
  
  visited = [] # 방문 한 노드 리스트 (구현 필수 X -> 문제에 따라 적절한 타입 정의 및 구현하기)
  
  q = deque() # 방문 예정인 노드 리스트
  q.append(root)

  while q: # q(방문 예정 리스트)에 노드가 존재할 때 까지 반복
    cur_node = q.popleft() # 노드에 접근
    visited.append(cur_node.value) # 현재 노드에 방문

    if cur_node.left:
      q.append(cur_node.left)
    if cur_node.right:
      q.append(cur_node.right)

  return visited