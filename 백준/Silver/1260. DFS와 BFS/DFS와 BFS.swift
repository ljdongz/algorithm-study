import Foundation



func bfs(graph: [[Int]], v: Int) {
  var visited: [Bool] = Array(repeating: false, count: N+1)
  visited[v] = true
  var q: [Int] = [v]
  var result = "\(v) "
  
  while !q.isEmpty {
    let cur = q.removeFirst()
    
    for next in graph[cur] {
      if !visited[next] {
        visited[next] = true
        result += "\(next) "
        q.append(next)
      }
    }
  }
  
  print(result)
}

func dfs(graph: [[Int]], v: Int) {
  var visited: [Bool] = Array(repeating: false, count: N+1)
  var result = ""
  
  func recursive(v: Int) {
    visited[v] = true
    result += "\(v) "
    for next in graph[v] {
      if !visited[next] {
        recursive(v: next)
      }
    }
  }
  
  recursive(v: v)
  print(result)
}

let values = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = values[0]
let M = values[1]
let V = values[2]

var graph: [[Int]] = Array(repeating: [], count: N+1)

for _ in 0..<M {
  let nodes = readLine()!.split(separator: " ").map { Int(String($0))! }
  let x = nodes[0]
  let y = nodes[1]
  
  graph[x].append(y)
  graph[y].append(x)
  
  graph[x].sort()
  graph[y].sort()
}

dfs(graph: graph, v: V)
bfs(graph: graph, v: V)
