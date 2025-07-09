import Foundation

let input = Int(readLine()!)!

let numbers = readLine()!.split(separator: " ").map { Int($0)! }

var minimum = Int.max
var maximum = Int.min

for num in numbers {
  minimum = min(minimum, num)
  maximum = max(maximum, num)
}

print(minimum, maximum)