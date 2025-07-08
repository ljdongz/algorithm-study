import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }

var cards = readLine()!.split(separator: " ").map { Int($0)! }
var result = 0

for i in 0..<(input[0] - 2) {
  for j in (i+1)..<(input[0] - 1) {
    for k in (j+1)..<input[0] {
      let sum = cards[i] + cards[j] + cards[k]
      if sum <= input[1] {
        result = max(result, sum)
      }
    }
  }
}

print(result)

