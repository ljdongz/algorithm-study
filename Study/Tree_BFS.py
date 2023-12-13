from collections import deque

class Node:
  def __init__(self, value, left = None, right = None) -> None:
    self.left = left
    self.right = right
    self.value = value

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

# (Graph 탐색처럼) visited에 방문할 노드를 미리 추가한 방법
def bfs2(root):

  if root is None:
    return []
  
  visited = [root.value]

  q = deque() # 방문 예정인 노드 리스트
  q.append(root)

  while q: # q(방문 예정 리스트)에 노드가 존재할 때 까지 반복
    cur_node = q.popleft() # 노드에 접근

    if cur_node.left:
      q.append(cur_node.left)
      visited.append(cur_node.left.value)
    if cur_node.right:
      q.append(cur_node.right)
      visited.append(cur_node.right.value)


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.right.right = Node(10)