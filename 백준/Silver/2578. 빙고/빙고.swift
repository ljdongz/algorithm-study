import Foundation

var bingoList = [
  [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
  [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]
]

for row in 0..<5 {
  var rowBingo: [(Int, Int)] = []
  var colBingo: [(Int, Int)] = []
  for col in 0..<5 {
    rowBingo.append((col, row))
    colBingo.append((row, col))
  }

  bingoList.append(rowBingo)
  bingoList.append(colBingo)
}

var dict: [Int: (Int, Int)] = [:]
var bingoCount = 0
var callCount = 0

for row in 0..<5 {
  let input = readLine()!.split(separator: " ").map { Int($0)! }

  for col in 0..<5 {
    dict[input[col]] = (row, col)
  }
}


for _ in 0..<5 {
  let input = readLine()!.split(separator: " ").map { Int($0)! }

  for number in input {
    if bingoCount == 3 { break }
    callCount += 1

    let (row, col) = dict[number]!

    for i in 0..<bingoList.count {
      if bingoCount == 3 { break }
      if bingoList[i].isEmpty { continue }
      
      bingoList[i].removeAll { $0 == (row, col) }
      if bingoList[i].isEmpty { bingoCount += 1 }
    }
  }
}


print(callCount)