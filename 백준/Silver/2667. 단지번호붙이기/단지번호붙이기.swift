import Foundation

let n = Int(readLine()!)!

var graph: [[Int]] = []
var visited: [[Bool]] = Array(
  repeating: Array(repeating: false, count: n), 
  count: n
)
var drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

var result: [Int] = []

for _ in 0..<n {
  let input = readLine()!.map { Int(String($0))! }
  graph.append(input)
}

for row in 0..<n {
  for col in 0..<n {
    if graph[row][col] == 0 { continue }
    if visited[row][col] { continue }

    var queue: [(Int, Int)] = []
    var front = 0
    
    visited[row][col] = true

    queue.append((row, col))
    var count = 0

    while queue.count >= front + 1 {
      let (curR, curC) = queue[front]
      front += 1
      count += 1

      for (r, c) in drdc {
        let nextR = curR + r
        let nextC = curC + c

        if nextR >= 0 && nextR < n && nextC >= 0 && nextC < n {
          if graph[nextR][nextC] != 0 && !visited[nextR][nextC] {
            queue.append((nextR, nextC))
            visited[nextR][nextC] = true
          }
        }
      }
    }

    result.append(count)
  }
}

print(result.count)
result.sort()
for i in 0..<result.count {
  print(result[i])
}
