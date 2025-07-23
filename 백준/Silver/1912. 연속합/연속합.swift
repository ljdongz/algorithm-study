import Foundation

let n = Int(readLine()!)!
let nums = readLine()!.split(separator: " ").map { Int(String($0))! }

var memo = Array(repeating: Int.min, count: n)

func recursive(idx: Int) -> Int {
  if idx == n { return 0 }

  if memo[idx] != Int.min { return memo[idx] }

  let result = recursive(idx: idx + 1)

  memo[idx] = max(nums[idx] + result, nums[idx])
  return memo[idx]
}

_ = recursive(idx: 0)
print(memo.max()!)