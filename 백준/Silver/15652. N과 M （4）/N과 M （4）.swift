import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let m = input[1]
var nums: [Int] = []

func recursive(cur: Int, start: Int) {
  if cur == m {
    for num in nums {
      print(num, terminator: " ")
    }
    print()
    return
  }

  for i in start..<n {
    nums.append(i+1)
    recursive(cur: cur + 1, start: i)
    nums.removeLast()
  }
}

recursive(cur: 0, start: 0)