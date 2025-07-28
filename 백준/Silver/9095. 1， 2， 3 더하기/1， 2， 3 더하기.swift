import Foundation

let n = Int(readLine()!)!

var result = 0

func recursive(target: Int, cur: Int) {
  if cur > target { return }
  if cur == target { result += 1; return }

  for i in 1...3 {
    recursive(target: target, cur: cur + i)
  }
}

for _ in 0..<n {
  let input = Int(readLine()!)!
  recursive(target: input, cur: 0)
  print(result)
  result = 0
}

