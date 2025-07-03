import Foundation

let alphabet = [
  "A", "B", "C", "D", "E", 
  "F", "G", "H", "I", "J", 
  "K", "L", "M", "N", "O", 
  "P", "Q", "R", "S", "T",
  "U", "V", "W", "X", "Y", "Z"
]

var dict: [String: Int] = [:]

for i in 0..<alphabet.count {
  dict[alphabet[i]] = i + 1
}

let N = Int(readLine()!)!

var result = ""

for n in 0..<N {
  let input = readLine()!.split(separator: " ").map { String($0) }
  let first = input[0].map { String($0) }
  let second = input[1].map { String($0) }

  result += "Distances:"

  for i in 0..<first.count {
    let x = dict[first[i]]!
    let y = dict[second[i]]!

    if x <= y {
      result += " \(y-x)"
    } else {
      result += " \(y + 26 - x)"
    }
  }

  if n != N - 1 {
    result += "\n"
  }
}

print(result)