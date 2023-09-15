from collections import deque

def bfs(root):
  visited = []
  if root is None:
    return []
  q = deque() # 노드 접근을 위한 큐
  q.append(root)

  while q: # q에 노드가 존재할 때 까지 반복
    cur_node = q.popleft() # 노드에 접근
    visited.append(cur_node.value) # 현재 노드에 방문

    if cur_node.left:
      q.append(cur_node.left)
    if cur_node.right:
      q.append(cur_node.right)

  return visited