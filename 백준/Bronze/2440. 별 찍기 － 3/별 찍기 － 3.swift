import Foundation

let N = Int(readLine()!)!

var result = ""

for i in stride(from: N, to: 0, by: -1) {
  for j in 1...N {
    if j > i { continue }

    result += "*"
  }

  if i != 1 { result += "\n" }
}

print(result)