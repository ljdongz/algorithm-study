import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let m = input[1]

var visited: [Bool] = .init(repeating: false, count: n + 1)
var current: [Int] = []

func recursive(k: Int) {
  if k == m {
    // 출력
    for i in 0..<m {
      print("\(current[i])", terminator: " ")
    }
    print()
    return
  }

  for i in 1...n {
    if !visited[i] {
      visited[i] = true
      current.append(i)
      recursive(k: k + 1)
      current.removeLast()
      visited[i] = false
    }
  }
}

recursive(k: 0)