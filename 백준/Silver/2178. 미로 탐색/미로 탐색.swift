import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let m = input[1]

var visited: [[Int]] = .init(
  repeating: .init(repeating: 0, count: m), 
  count: n
)
var drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
var board: [[Int]] = []

for _ in 0..<n {
  let input = readLine()!.map { Int(String($0))! }
  board.append(input)
}

var queue: [(Int, Int)] = []
queue.append((0, 0))
var front = 0
visited[0][0] = 1

while queue.count >= front + 1 {
  let (curR, curC) = queue[front]
  front += 1

  for (dr, dc) in drdc {
    let nextR = curR + dr
    let nextC = curC + dc

    if nextR >= 0 && nextR < n && nextC >= 0 && nextC < m {
      if visited[nextR][nextC] == 0 && board[nextR][nextC] == 1 {
        queue.append((nextR, nextC))
        visited[nextR][nextC] = visited[curR][curC] + 1
      }
    }
  }
}

print(visited[n - 1][m - 1])