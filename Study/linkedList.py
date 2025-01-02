
class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next
    

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, value):
    node = Node(value)

    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node

  def removeLast(self):
    if self.head is None:
      return
    
    if self.head.next is None:
      self.head = None
      self.tail = None
      return
    
    cur = self.head
    while cur.next.next is not None:
      cur = cur.next

    cur.next = None
    self.tail = cur

  def remove(self, index):
    if self.head is None:
      return
    
    if index == 0:
      self.head = self.head.next
      if self.head is None:
        self.tail = None
      return

    cur = self.head
    for _ in range(index-1):
      if cur.next.next is None:
        return
      cur = cur.next
  
    tmp = cur.next
    cur.next = cur.next.next
    
    if self.tail == tmp:
      self.tail = cur

  def print(self):
    if self.head is None:
      print("first and last is None")
      return
    
    print("first:", self.head.value)
    print("last:", self.tail.value)

    cur = self.head
    while cur is not None:
      print(cur.value)
      cur = cur.next


linkedList = LinkedList()

linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.remove(1)
linkedList.remove(2)
linkedList.print()
linkedList.remove(0)

linkedList.print()