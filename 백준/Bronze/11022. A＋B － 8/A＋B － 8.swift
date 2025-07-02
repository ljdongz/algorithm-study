import Foundation

let T = Int(readLine()!)!

var result: [String] = []
for i in 1...T {
  let input = readLine()!.split(separator: " ").map { Int($0)! }
  result.append("Case #\(i): \(input[0]) + \(input[1]) = \(input[0] + input[1])")
}

for res in result {
  print(res)
}