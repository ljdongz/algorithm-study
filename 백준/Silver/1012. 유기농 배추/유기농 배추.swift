import Foundation

let drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in 0..<Int(readLine()!)! {
  let input = readLine()!.split(separator: " ").map { Int(String($0))! }

  let M = input[0]
  let N = input[1]
  let K = input[2]

  var board: [[Int]] = .init(
    repeating: .init(
      repeating: 0,
      count: M
    ),
    count: N
  )
  var result = 0

  for _ in 0..<K {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    let col = input[0]
    let row = input[1]

    board[row][col] = 1
  }

  for row in 0..<N {
    for col in 0..<M {

      if board[row][col] != 1 { continue }
      result += 1
      var queue: [(Int, Int)] = [(row, col)]
      var front = 0

      while queue.count >= front + 1 {
        let (curR, curC) = queue[front]
        front += 1

        for (dr, dc) in drdc {
          let nextR = curR + dr
          let nextC = curC + dc

          if nextR < 0 || nextR >= N || nextC < 0 || nextC >= M { continue }
          if board[nextR][nextC] != 1 { continue }

          queue.append((nextR, nextC))
          board[nextR][nextC] = 0
        }
      }
    }
  }

  print(result)
}

