import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let m = input[1]
let nums = readLine()!.split(separator: " ").map { Int(String($0))! }.sorted()
var visited: [Bool] = .init(repeating: false, count: n)
var result: [Int] = .init(repeating: 0, count: m)
var answer = ""


func recursive(k: Int) {
  if k == m {
    answer += result.map { String($0) }.joined(separator: " ") + "\n"
    return
  }

  var used = 0

  for i in 0..<n {
    if !visited[i] {
      if used == nums[i] { continue }
      visited[i] = true
      result[k] = nums[i]
      used = nums[i]
      recursive(k: k + 1)
      visited[i] = false
    }
  }
}

recursive(k: 0)
print(answer)