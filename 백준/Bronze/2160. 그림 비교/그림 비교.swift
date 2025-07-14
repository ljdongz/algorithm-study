import Foundation

let N = Int(readLine()!)!

var boards: [[String]] = []

var result: (Int, Int) = (0, 0)
var diff = 36

for _ in 0..<N {
  var board: [String] = []
  for _ in 0..<5 {
    board.append(contentsOf: readLine()!.map { String($0) })
  }
  boards.append(board)
}

// 첫번째 보드
for i in 0..<(boards.count - 1) {
  // 두번째 보드
  for j in (i+1)..<boards.count {
    
    var currentDiff = 0
    // 두 보드의 각 칸을 비교
    for k in 0..<35 {

      // 칸이 서로 다른 경우
      if boards[i][k] != boards[j][k] {
        currentDiff += 1
      }
    }

    // 현재 비교한 개수의 차이가 이전에 차이보다 적은 경우
    if currentDiff < diff {
      result = (i + 1, j + 1)
      diff = currentDiff
    }
  }
}

print(result.0, result.1)