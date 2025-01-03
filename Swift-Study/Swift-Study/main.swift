//
//  main.swift
//  Swift-Study
//
//  Created by 이정동 on 1/3/25.
//

import Foundation


var list = DoublyLinkedList<Int>()
list.append(1)
list.append(2)
list.print()
list.remove(at: 0)
list.print()
list.remove(at: 1)
list.print()
list.remove(at: 0)
list.print()
