import Foundation

let n = Int(readLine()!)!

var visited: [[Bool]] = []
var drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
var board: [[Int]] = []

for _ in 0..<n {
  let input = readLine()!.split(separator: " ").map { Int(String($0))! }
  board.append(input)
}

var result: Int = 1

for height in 1...100 {
  visited = Array(
    repeating: Array(repeating: false, count: n), 
    count: n
  )
  var count = 0
  for row in 0..<n {
    for col in 0..<n {
      
      if visited[row][col] || board[row][col] <= height { continue }
      bfs(row: row, col: col, height: height)
      count += 1
    }
  }

  result = max(result, count)
}

func bfs(row: Int, col: Int, height: Int) {
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
        if !visited[nextRow][nextCol] && board[nextRow][nextCol] > height {
          queue.append((nextRow, nextCol))
          visited[nextRow][nextCol] = true
        }
      }
    }
  }
}

print(result)