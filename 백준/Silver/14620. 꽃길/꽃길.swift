import Foundation

let n = Int(readLine()!)!

var flowers: [[Int]] = []
var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: n), count: n)
var result = Int.max
let dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in 0..<n {
  flowers.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

func recursive(count: Int, sum: Int, row: Int, col: Int, visited: [[Bool]]) {
  if visited[row][col] { return }
  
  if count == 3 {
    result = min(result, sum)
    return
  }
  
  for i in row..<n {
    for j in col..<n {
      if visited[i][j] { continue }

      var visited = visited
      visited[i][j] = true
      var sum = sum + flowers[i][j]

      var flag = false

      for (r, c) in dir {
        let nextRow = i + r
        let nextCol = j + c

        if nextRow >= 0 && nextRow < n && nextCol >= 0 && nextCol < n && !visited[nextRow][nextCol] {
          visited[nextRow][nextCol] = true
          sum += flowers[nextRow][nextCol]
        } else {
          flag = true
        }
      }

      if !flag {
        recursive(count: count + 1, sum: sum, row: row, col: col, visited: visited)
      }

    }
  }
}

recursive(count: 0, sum: 0, row: 0, col: 0, visited: visited)
print(result)