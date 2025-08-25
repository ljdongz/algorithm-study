import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let m = input[1]

var visited: [[Bool]] = .init(
  repeating: .init(repeating: false, count: m), 
  count: n
)
var drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
var board: [[Int]] = []

for _ in 0..<n {
  let input = readLine()!.map { Int(String($0))! }
  board.append(input)
}

var queue: [(Int, Int, Int)] = []
queue.append((0, 0, 1))
var front = 0
visited[0][0] = true

while queue.count >= front + 1 {
  let (curR, curC, count) = queue[front]
  front += 1

  if curR == n - 1 && curC == m - 1 {
    print(count)
  }

  for (dr, dc) in drdc {
    let nextR = curR + dr
    let nextC = curC + dc

    if nextR >= 0 && nextR < n && nextC >= 0 && nextC < m {
      if !visited[nextR][nextC] && board[nextR][nextC] == 1 {
        queue.append((nextR, nextC, count + 1))
        visited[nextR][nextC] = true
      }
    }
  }
}
