import Foundation

let N = Int(readLine()!)!

var result = ""

for i in 1...N {
  for j in 1...(N * 2) {
    if j <= i || j >= (N * 2) - i + 1 { result += "*" }
    else { result += " "}
  }

  result += "\n"
}

for i in stride(from: N-1, to: 0, by: -1) {
  for j in 1...(N * 2) {
    if j <= i || j >= (N * 2) - i + 1 { result += "*" }
    else { result += " "}
  }

  if i != 1 { result += "\n" }
}

print(result)
