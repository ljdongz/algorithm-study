import Foundation

let N = readLine()!.split(separator: " ").map { Int(String($0))! }
let x = N[0]
let y = N[1]

var members = Set<String>()

for _ in 0..<x {
  let input = readLine()!
  
  members.insert(input)
}

var result: [String] = []

for _ in 0..<y {
  let input = readLine()!
  if members.contains(input) { 
    result.append(input)
  }
}

result.sort()
print(result.count)
result.forEach { print($0) }