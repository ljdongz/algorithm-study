//
//  Graph_BFS.swift
//  Swift-Study
//
//  Created by 이정동 on 1/6/25.
//

import Foundation


private let N = 10

func bfs(graph: [[Int]], v: Int) {
  var visited: [Bool] = Array(repeating: false, count: N+1)
  visited[v] = true
  var q: [Int] = [v]
  
  while !q.isEmpty {
    let cur = q.removeFirst()
    
    for next in graph[cur] {
      if !visited[next] {
        visited[next] = true
        q.append(next)
      }
    }
  }
}


