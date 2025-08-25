import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let M = input[0]
let N = input[1]

let drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
var queue: [(Int, Int)] = []
var front = 0
var count = 0
var visited: [[Bool]] = .init(
  repeating: .init(
    repeating: false,
    count: M
  ),
  count: N
)
var board: [[Int]] = []
for r in 0..<N {
  let input = readLine()!.split(separator: " ").map { Int(String($0))! }
  for c in 0..<input.count {
    if input[c] == 1 { 
      queue.append((r, c)) 
      visited[r][c] = true
    }
  }
  board.append(input)
}


while !queue.isEmpty {
  let tempQueue = queue
  var flag = false
  queue = []

  if tempQueue.isEmpty { continue }
  
  for (curR, curC) in tempQueue {
    board[curR][curC] = 1
    for (dr, dc) in drdc {
      let nextR = curR + dr
      let nextC = curC + dc

      if nextR >= 0 && nextR < N && nextC >= 0 && nextC < M {
        if !visited[nextR][nextC] && board[nextR][nextC] == 0 {
          flag = true
          queue.append((nextR, nextC))
          visited[nextR][nextC] = true
        }
      }
    }
  }

  if flag { count += 1 }
}
  
var succeed = true
out: for r in 0..<N {
  for c in 0..<M {
    if board[r][c] == 0 { 
      succeed = false 
      break out
    } 
  }
}

if succeed {
  print(count)
} else {
  print(-1)
}