//
//  DoublyLinkedList.swift
//  Swift-Study
//
//  Created by 이정동 on 1/3/25.
//

import Foundation

class DoublyLinkedList<T> {
  class Node: Equatable {
    static func == (lhs: DoublyLinkedList<T>.Node, rhs: DoublyLinkedList<T>.Node) -> Bool {
      lhs.next == rhs.next && lhs.prev == rhs.prev
    }
    
    var prev: Node?
    var next: Node?
    var value: T
    
    init(prev: Node? = nil, next: Node? = nil, value: T) {
      self.prev = prev
      self.next = next
      self.value = value
    }
  }
  
  var head: Node?
  var tail: Node?
  
  func append(_ value: T) {
    var node = Node(value: value)
    
    if head == nil {
      self.head = node
      self.tail = node
      return
    }
    
    node.prev = tail
    self.tail?.next = node
    self.tail = node
  }
  
  func removeLast() {
    if head == nil {
      return
    }
    
    self.tail = self.tail?.prev
    self.tail?.next = nil
    
    if self.tail == nil {
      self.head = nil
    }
  }
  
  func remove(at index: Int) {
    if head == nil { return }
    
    if index == 0 {
      self.head = self.head?.next
      if self.head == nil {
        self.tail = nil
      }
      return
    }
    
    var cur = self.head
    for _ in 0..<index-1 {
      if cur?.next?.next == nil { return }
      cur = cur?.next
    }
    
    var target = cur?.next
    cur?.next = target?.next
    target?.next?.prev = cur
    
    if target == self.tail {
      self.tail = cur
    }
  }
  
  func print() {
    Swift.print(self.head?.value, self.tail?.value)
  }
}
