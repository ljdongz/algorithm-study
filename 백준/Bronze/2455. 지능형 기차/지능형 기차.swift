import Foundation

var current = 0
var result = 0

for _ in 0..<4 {
  let input = readLine()!.split(separator: " ").map { Int($0)! }

  current += (input[1] - input[0])

  result = max(result, current)
}

print(result)