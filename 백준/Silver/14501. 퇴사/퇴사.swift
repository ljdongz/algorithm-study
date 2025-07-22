import Foundation

let n = Int(readLine()!)!

var meets: [[Int]] = [[]]
var dp: [Int] = .init(repeating: 0, count: n + 2)
var result = 0

for _ in 0..<n {
  meets.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

func recursive(cur: Int, sum: Int) {

  if cur > n {
    result = max(result, sum)
    return
  }

  for i in 0..<(n - cur + 1) {
    let meet = meets[cur]
    let due = meet[0]
    let price = meet[1]

    if cur + due + i - 1 <= n {
      recursive(cur: cur + due + i, sum: sum + price)
    }
  }
}

for i in 1...n {
  recursive(cur: i, sum: 0)
}

print(result)