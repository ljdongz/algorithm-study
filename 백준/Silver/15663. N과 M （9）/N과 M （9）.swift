import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let m = input[1]

let nums = readLine()!.split(separator: " ").map { Int(String($0))! }.sorted()
var called: Set<[Int]> = Set<[Int]>()
var visited: [Bool] = .init(repeating: false, count: n)
var curr: [Int] = []

func recursive(count: Int) {
  if count == m {
    if !called.contains(curr) {
      called.insert(curr)
      for c in curr {
        print(c, terminator: " ")
      }
      print()
    }
    return
  }

  for i in 0..<n {
    if !visited[i] {
      visited[i] = true
      curr.append(nums[i])
      recursive(count: count + 1)
      curr.removeLast()
      visited[i] = false
    }
  }
}

recursive(count: 0)
