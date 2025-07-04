import Foundation

let N = Int(readLine()!)!

var numbers: [[Int]] = []

for _ in 0..<N {
  let input = readLine()!.split(separator: " ").map { Int(String($0))! }
  numbers.append(input)
}

numbers.sort { ($0[0], $0[1]) < ($1[0], $1[1]) }

numbers.forEach { print("\($0[0]) \($0[1])") }