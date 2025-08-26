import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let M = input[0]
let N = input[1]
let H = input[2]

let dhdrdc = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

var visited: [[[Int]]] = .init(
  repeating: .init(
    repeating: .init(
      repeating: -1,
      count: M
    ),
    count: N
  ),
  count: H
)
var board: [[[Int]]] = []
var queue: [(Int, Int, Int)] = []
var front = 0

for height in 0..<H {
  var temp: [[Int]] = []
  for row in 0..<N {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    temp.append(input)

    for col in 0..<M {
      if input[col] == 1 {
        queue.append((height, row, col))
        visited[height][row][col] = 0
      } else if input[col] == -1 {
        visited[height][row][col] = -2
      }
    }
  }

  board.append(temp)
}

while queue.count >= front + 1 {
  let (curH, curR, curC) = queue[front]
  front += 1

  for (dh, dr, dc) in dhdrdc {
    let nextH = curH + dh
    let nextR = curR + dr
    let nextC = curC + dc

    if nextH < 0 || nextH >= H || nextR < 0 || nextR >= N || nextC < 0 || nextC >= M { continue }
    if board[nextH][nextR][nextC] == -1 || visited[nextH][nextR][nextC] != -1 { continue }

    queue.append((nextH, nextR, nextC))
    visited[nextH][nextR][nextC] = visited[curH][curR][curC] + 1
  }
}

var flag = false
var result = 0
out: for height in 0..<H {
  for row in 0..<N {
    for col in 0..<M {
      result = max(result, visited[height][row][col])
      if visited[height][row][col] == -1 {
        flag = true
        break out
      }
    }
  }
}

if flag {
  print(-1)
} else {
  print(result)
}