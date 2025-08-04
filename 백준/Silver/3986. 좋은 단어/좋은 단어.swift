import Foundation

let n = Int(readLine()!)!

var result = 0

for _ in 0..<n {
  var stack: [String] = []

  let input = readLine()!.map { String($0) }

  for c in input {
    if stack.isEmpty {
      stack.append(c)
    } else if stack.last! == c {
      _ = stack.popLast()
    } else {
      stack.append(c)
    }
  }

  if stack.isEmpty { result += 1 }
}

print(result)