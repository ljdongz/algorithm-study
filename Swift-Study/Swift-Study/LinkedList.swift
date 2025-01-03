//
//  LinkedList.swift
//  Swift-Study
//
//  Created by 이정동 on 1/3/25.
//

import Foundation

class LinkedList<T> {
  class Node {
    var next: Node?
    var value: T
    
    init(next: Node? = nil, value: T) {
      self.next = next
      self.value = value
    }
  }
  
  var head: Node?
  var tail: Node?
  
  func append(value: T) {
    let node = Node(value: value)
    
    if head == nil {
      self.head = node
      self.tail = node
      return
    }
    
    self.tail?.next = node
    self.tail = node
  }
  
  func removeLast() {
    if self.head == nil {
      return
    }
    
    if self.head?.next == nil {
      self.head = nil
      self.tail = nil
      return
    }
    
    var cur = head
    while cur?.next?.next != nil {
      cur = cur?.next
    }
    
    cur?.next = nil
    self.tail = cur
  }
  
  func remove(at index: Int) {
    if self.head == nil {
      return
    }
    
    if index == 0 {
      self.head = self.head?.next
      if self.head == nil {
        self.tail = nil
      }
      return
    }
    
    var cur = self.head
    for _ in 0..<index-1 {
      if cur?.next?.next == nil {
        return
      }
      cur = cur?.next
    }
    
    cur?.next = nil
    self.tail = cur
  }
  
  func print() {
    Swift.print(self.head?.value, self.tail?.value)
  }
}
