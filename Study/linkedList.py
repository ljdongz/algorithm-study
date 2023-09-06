class Node:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev


class BrowserHistory:
  def __init__(self, value):
    node = Node(value)
    self.head = node
    self.tail = node

    print("None")

  def visit(self, value):
    node = Node(value)
    self.tail.next = node
    node.prev = self.tail
    self.tail = self.tail.next

    print("None")

  def back(self, value):
    node = self.tail
    
    for _ in range(value):
      if node.prev is None:
        break
      node = node.prev
    
    self.tail = node

    print(self.tail.value)

  def forward(self, value):
    node = self.tail
    
    for _ in range(value):
      if node.next is None:
        break
      node = node.next
    
    self.tail = node

    print(self.tail.value)


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)