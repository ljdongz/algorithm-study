import Foundation

let N = Int(readLine()!)!

var numbers: [(Int, String)] = []

for _ in 0..<N {
  let input = readLine()!.split(separator: " ").map { String($0) }
  numbers.append((Int(input[0])!, input[1]))
}

numbers.sort { $0.0 < $1.0 }

numbers.forEach { print("\($0.0) \($0.1)") }