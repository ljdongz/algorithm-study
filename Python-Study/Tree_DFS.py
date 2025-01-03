
# DFS(깊이 우선 탐색) 기본 개념
def dfs(cur_node):
  if cur_node is None:
    return
  dfs(cur_node.left)
  dfs(cur_node.right)

# 전위 순회 (Left Node 방문 전 나 자신 리턴)
def preorder(cur_node):
  if cur_node is None:
    return
  
  print(cur_node.value)
  preorder(cur_node.left)
  preorder(cur_node.right)

# 중위 순회 (Left Node 방문 후 시 나 자신 리턴)
def inorder(cur_node):
  if cur_node is None:
    return
  
  inorder(cur_node.left)
  print(cur_node.value)
  inorder(cur_node.right)

# 후위 순회 (Left, Right Node 방문 후 나 자신 리턴))
def postorder(cur_node):
  if cur_node is None:
    return
  
  postorder(cur_node.left)
  postorder(cur_node.right)
  print(cur_node.value)