import Foundation

let n = Int(readLine()!)!

var board: [[String]] = []

let dy = [-1, 0, 1, 0]
let dx = [0, 1, 0, -1]

for _ in 0..<n {
  board.append(readLine()!.map { String($0) })
}

// 2) 변경된 board를 기준으로 행과 열을 돌면서, 먹을 수 있는(연속된) 사탕의 최대 개수
var result = 0

for y in 0..<n {
  for x in 0..<n {
    // 상하좌우의 값과 현재 좌표값을 변경하는 로직

    for dir in 0..<4 {
      let ny = y + dy[dir]
      let nx = x + dx[dir]

      if nx >= 0 && nx < n && ny >= 0 && ny < n {
        
        let temp = board[y][x]
        board[y][x] = board[ny][nx]
        board[ny][nx] = temp

        let count = check()
        result = max(result, count)
        
        board[ny][nx] = board[y][x]
        board[y][x] = temp
      }
    }
  }
}


func check() -> Int {
  var answer = 0

  for y in 0..<n {
    var count = 1

    for x in 1..<n {
      if board[y][x] == board[y][x-1] { 
        count += 1 
      } else {
        answer = max(answer, count)
        count = 1
      }
    }

    answer = max(answer, count)
  }

  for x in 0..<n {
    var count = 1

    for y in 1..<n {
      if board[y][x] == board[y-1][x] {
        count += 1
      } else {
        answer = max(answer, count)
        count = 1
      }
    }

    answer = max(answer, count)
  }

  return answer
}

print(result)