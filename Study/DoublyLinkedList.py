
class Node:
  def __init__(self, value):
    self.prev = None
    self.next = None
    self.value = value

class DoublyLinkedList:
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
      node.prev = self.tail
      self.tail = node

  def removeLast(self):
    if self.head is None:
      return
    
    self.tail = self.tail.prev
    
    if self.tail is None:
      self.head = None
    else:
      self.tail.next = None

  def remove(self, index):
    if self.head is None:
      return
    
    if index == 0:
      self.head = self.head.next
      if self.head is None:
        self.tail = None

    cur = self.head
    for _ in range(index):
      if cur.next is None:
        return
      cur = cur.next

    cur.prev.next = cur.next

    if cur.next is None:
      self.tail = cur.prev


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


list = DoublyLinkedList()
list.append(1)
list.append(2)
list.append(3)
list.remove(1)
list.remove(2)
list.print()