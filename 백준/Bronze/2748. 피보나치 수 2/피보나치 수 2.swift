import Foundation

let n = Int(readLine()!)!
var dp: [Int: Int] = [:]

func fibo(_  n: Int) -> Int {
  if n <= 1 { return n }

  if let value = dp[n] {
    return value
  }

  let result = fibo(n-1) + fibo(n-2)
  dp[n] = result
  return result
}

print(fibo(n))