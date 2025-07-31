import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let k = input[1]

var bags: [(w: Int, v: Int)] = []
var dp: [[Int]] = .init(repeating: .init(repeating: -1, count: k + 1), count: n + 1)

for _ in 0..<n {
  let input = readLine()!.split(separator: " ").map { Int(String($0))! }
  bags.append((w: input[0], v: input[1]))
}

func recursive(idx: Int, w: Int) -> Int {
  if idx == n { return 0 }
  if dp[idx][w] != -1 { return dp[idx][w] }

  var take = 0
  if w + bags[idx].w <= k {
    take = recursive(idx: idx + 1, w: w + bags[idx].w) + bags[idx].v
  }

  let skip = recursive(idx: idx + 1, w: w)

  dp[idx][w] = max(take, skip)
  return dp[idx][w]
}

print(recursive(idx: 0, w: 0))
