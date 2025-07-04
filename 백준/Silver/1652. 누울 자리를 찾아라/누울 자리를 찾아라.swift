import Foundation

let N = Int(readLine()!)!

var room = Array(repeating: Array(repeating: "", count: N), count: N)

var rowCount = 0
var colCount = 0

for r in 0..<N {
  let columns = readLine()!.map { String($0) }

  for c in 0..<N {
    room[r][c] = columns[c]
  }
}

for r in 0..<N {
  var rowString = ""

  for c in 0..<N {
    rowString += "\(room[r][c])"
  }

  let splits = rowString.split(separator: "X")

  for sp in splits {
    if sp != "." { rowCount += 1 }
  }
}

for c in 0..<N {
  var colString = ""

  for r in 0..<N {
    colString += "\(room[r][c])"
  }

  let splits = colString.split(separator: "X")

  for sp in splits {
    if sp != "." { colCount += 1 }
  }
}

print("\(rowCount) \(colCount)")