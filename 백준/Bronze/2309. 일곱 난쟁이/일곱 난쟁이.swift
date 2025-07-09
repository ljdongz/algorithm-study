import Foundation

var array: [Int] = []

for _ in 0..<9 {
  array.append(Int(readLine()!)!)
}

let total = array.reduce(0) { $0 + $1 }

for i in 0..<(array.count - 1) {
  for j in (i+1)..<(array.count) {
    let a = array[i]
    let b = array[j]
    if total - a - b == 100 {
      array.removeAll { $0 == a || $0 == b }
      break
    }
  }

  if array.count == 7 { break }
}

array.sort()

array.forEach { print($0) }