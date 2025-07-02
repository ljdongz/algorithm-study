import Foundation

let input = readLine()!.map { String($0) }

var result = ""
for i in 0..<input.count {
  if i != 0 && i % 10 == 0 { result += "\n" }
  result += input[i]
}

print(result)