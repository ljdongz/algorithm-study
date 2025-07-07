import Foundation

let N = Int(readLine()!)!

var mirror: [[String]] = []

for _ in 0..<N {
  let input = readLine()!.map { String($0) }
  mirror.append(input)
}

let K = Int(readLine()!)!
var result = ""

for i in 0..<N {
  for j in 0..<N {
    if K == 1 {
      result += mirror[i][j]
    } else if K == 2 {
      result += mirror[i][N-j-1] 
    } else {
      result += mirror[N-i-1][j]
    }
  }

  result += "\n"
}

print(result)

