import Foundation

let N = Int(readLine()!)!

var result = ""

for i in 1...N {
  for j in 1...N {
    if i + j > N { result += "*" }
    else { result += " "}
  }

  if i != N { result += "\n" }
}

print(result)