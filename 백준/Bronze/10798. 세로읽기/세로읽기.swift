//
//  main.swift
//  algorithm
//
//  Created by 이정동 on 7/2/25.
//

import Foundation

import Foundation

var array: [[String]] = Array(repeating: [], count: 15)

for _ in 0..<5 {
  let str = readLine()!.map { String($0) }
  for j in 0..<str.count {
    array[j].append(str[j])
  }
}

var result = ""

for i in 0..<array.count {
  for j in 0..<array[i].count {
    result += array[i][j]
  }
}

print(result)
