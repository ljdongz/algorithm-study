import Foundation

let numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
let N = Int(readLine()!)!

var array: [String] = []

for _ in 0..<N {
  array.append(readLine()!)
}

array.sort {
  if $0.count == $1.count {
    let a = $0.map { String($0) }.filter { numbers.contains($0) }.reduce(0) { $0 + Int($1)! }
    let b = $1.map { String($0) }.filter { numbers.contains($0) }.reduce(0) { $0 + Int($1)! }

    if a == b {
      return $0 < $1
    } else {
      return a < b
    }
  } else {
    return $0.count < $1.count
  }
}

array.forEach { print($0) }