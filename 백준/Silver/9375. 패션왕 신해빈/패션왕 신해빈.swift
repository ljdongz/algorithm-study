import Foundation

let N = Int(readLine()!)!

var result = ""

for _ in 0..<N {
  var clothes: [String: Int] = [:]
  let num = Int(readLine()!)!

  for _ in 0..<num {
    let input = readLine()!.split(separator: " ").map { String($0) }
    clothes[input[1], default: 0] += 1
  }

  var count = 1
  clothes.forEach { count *= ($0.value + 1) }
  result += "\(count - 1)\n"
}

print(result)

