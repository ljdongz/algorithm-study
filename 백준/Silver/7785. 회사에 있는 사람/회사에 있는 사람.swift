import Foundation

let N = Int(readLine()!)!


var log: [String: Int] = [:]

for i in 0..<N {
  let input = readLine()!.split(separator: " ").map { String($0) }
  if input[1] == "enter" {
    log[input[0]] = i
  } else {
    log.removeValue(forKey: input[0])
  }
}

let sortedArray = log.sorted { 
  $0.key > $1.key
}

for arr in sortedArray {
  print(arr.0)
}