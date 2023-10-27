
# 후위 순위 문제 (LCA)
## p, q의 가장 낮은 공통 조상의 노드를 반환

class Node:
  def __init__(self, value, left = None, right = None) -> None:
    self.left = left
    self.right = right
    self.value = value

def LCA(root, p, q):
  if root == None:
    return None
  
  left = LCA(root.left, p, q)
  right = LCA(root.right, p, q)

  if root.value == p or root.value == q:
    return root
  elif left != None and right != None: # left, right 노드 모두 값이 있는 경우
    return root
  return left or right # left, right 둘 다 None이면 None, 아니면 값이 있는 노드 반환

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

node = LCA(root, 6, 4)
print(node.value)