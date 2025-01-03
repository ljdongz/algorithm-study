from collections import deque


# BFS
# Maximum Depth of Binary Tree

class Node:
  def __init__(self, value, left = None, right = None) -> None:
    self.left = left
    self.right = right
    self.value = value

  

def maxDepth(root: Node):
  if root is None:
    return 0
  
  max_depth = 0
  q = deque()
  q.append((root, 1))

  while q:
    cur_node, cur_depth = q.popleft()
    max_depth = cur_depth

    if cur_node.left:
      q.append((cur_node.left, cur_depth + 1))
    if cur_node.right:
      q.append((cur_node.right, cur_depth + 1))

  return max_depth

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

print(maxDepth(root))