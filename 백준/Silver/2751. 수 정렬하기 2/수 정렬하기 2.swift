import Foundation

let N = Int(readLine()!)!

var numbers: [Int] = []

for _ in 0..<N {
  numbers.append(Int(readLine()!)!)
}

numbers.sort()

numbers.forEach { print($0) }