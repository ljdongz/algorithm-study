import Foundation

let N = Int(readLine()!)!

var possible = Set<String>()

for i in 1...9 {
  for j in 1...9 {
    if i == j { continue }
    for k in 1...9  {
      if i == k || j == k { continue }
      possible.insert("\(i)\(j)\(k)")
    }
  }
}

for _ in 0..<N {
  let input = readLine()!.split(separator: " ").map { String($0) }

  let callNumber = input[0].map { String($0) } // ["3", "2", "4"]
  let strike = Int(input[1])!
  let ball = Int(input[2])!

  var current = Set<String>()

  for pos in possible {
    let number = pos.map { String($0) }

    var sCount = 0
    var bCount = 0

    for i in 0..<3 {
      if callNumber[i] == number[i] {
        sCount += 1
      } else if callNumber[i] != number[i] && number.contains(callNumber[i]) {
        bCount += 1
      }
    }

    if sCount == strike && bCount == ball && possible.contains(pos) {
      current.insert(pos)
    }
  }

  possible = current
}

print(possible.count)