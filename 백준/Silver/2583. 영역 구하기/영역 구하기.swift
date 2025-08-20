import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

let m = input[0]
let n = input[1]
let k = input[2]

var graph: [[Int]] = Array(
  repeating: Array(repeating: 0, count: n), 
  count: m
)
var visited: [[Bool]] = Array(
  repeating: Array(repeating: false, count: n), 
  count: m
)
var drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in 0..<k {
  let input = readLine()!.split(separator: " ").map { Int(String($0))! }

  let startX = input[0] 
  let startY = input[1]
  let endX = input[2]
  let endY = input[3]

  for dx in 0..<(endX - startX) {
    for dy in 0..<(endY - startY) {
      graph[startY + dy][startX + dx] = 1
    }
  }
}

var result: [Int] = []

for row in 0..<m {
  for col in 0..<n {

    if visited[row][col] || graph[row][col] != 0 { continue }
    var queue: [(Int, Int)] = []
    var front = 0
    visited[row][col] = true
    queue.append((row, col))

    var count = 0

    while queue.count >= front + 1 {
      let (curRow, curCol) = queue[front]
      front += 1
      count += 1
      graph[curRow][curCol] = 2

      for (dr, dc) in drdc {
        let nextRow = curRow + dr
        let nextCol = curCol + dc

        if nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n {
          if !visited[nextRow][nextCol] && graph[nextRow][nextCol] == 0 {
            queue.append((nextRow, nextCol))
            visited[nextRow][nextCol] = true
          }
        }
      }
    }

    result.append(count)
  }
}

print(result.count)
result.sort()
for c in result {
  print(c, terminator: " ")
}