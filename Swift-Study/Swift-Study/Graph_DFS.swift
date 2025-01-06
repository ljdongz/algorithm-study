//
//  Graph_DFS.swift
//  Swift-Study
//
//  Created by 이정동 on 1/6/25.
//

import Foundation

private let N = 10

func dfs(graph: [[Int]], v: Int) {
  var visited: [Bool] = Array(repeating: false, count: N+1)
  
  func recursive(v: Int) {
    visited[v] = true
    for next in graph[v] {
      if !visited[next] {
        recursive(v: next)
      }
    }
  }
  
  recursive(v: v)
}
