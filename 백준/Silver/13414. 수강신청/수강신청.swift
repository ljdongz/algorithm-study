import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let K = input[0]
let L = input[1]

var log: [String: Int] = [:]

for i in 0..<L {
  let stu = readLine()!

  log[stu, default: 0] = i
}

var result = ""

let sortedArray = log.sorted { $0.value < $1.value }

if sortedArray.count <= K {
  sortedArray.forEach { print($0.0) }
} else {
  (0..<K).forEach { print(sortedArray[$0].0) }  
}


