import Foundation


let input = readLine()!.split(separator: " ").map { Int($0)! }

let colors = [["W", "B"], ["B", "W"]]
var board: [[String]] = []

var result: [Int] = [0, 0]
var count = Int.max

for _ in 0..<input[0] {
  let input = readLine()!.map { String($0) }
  board.append(input)
}

for i in 0...(input[0] - 8) {
  for j in 0...(input[1] - 8) {

    var result = [0, 0]

    for row in 0..<8 {
      for col in 0..<8 {
        let target = board[row+i][col+j]

        if colors[0][(row + col) % 2] != target {
          result[0] += 1
        }

        if colors[1][(row + col) % 2] != target {
          result[1] += 1
        }
      }
    }

    count = min(count, result.min()!)
  }
}


print(count)


