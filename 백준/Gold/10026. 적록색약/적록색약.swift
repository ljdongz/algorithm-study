import Foundation

let n = Int(readLine()!)!

var visited: [[Bool]] = Array(
  repeating: Array(repeating: false, count: n), 
  count: n
)
var drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
var board: [[String]] = []

for _ in 0..<n {
  let input = readLine()!.map { String($0) }
  board.append(input)
}

var result: [Int] = [0, 0]

for row in 0..<n {
  for col in 0..<n {
    if visited[row][col] { continue }
    bfs(row: row, col: col, target: [board[row][col]])
    result[0] += 1
  }
}

for row in 0..<n {
  for col in 0..<n {
    visited[row][col] = false
    if board[row][col] == "R" {
      board[row][col] = "G"
    }
  }
}

for row in 0..<n {
  for col in 0..<n {
    if visited[row][col] { continue }
    bfs(row: row, col: col, target: [board[row][col]])
    result[1] += 1
  }
}

func bfs(row: Int, col: Int, target: [String]) {
  var queue: [(Int, Int)] = []
  var front = 0
  visited[row][col] = true
  queue.append((row, col))

  while queue.count >= front + 1 {
    let (curRow, curCol) = queue[front]
    front += 1

    for (dr, dc) in drdc {
      let nextRow = curRow + dr
      let nextCol = curCol + dc

      if nextRow >= 0 && nextRow < n && nextCol >= 0 && nextCol < n {
        if !visited[nextRow][nextCol] && target.contains(board[nextRow][nextCol]) {
          queue.append((nextRow, nextCol))
          visited[nextRow][nextCol] = true
        }
      }
    }
  }
}

print(result[0], result[1])