import Foundation

let N = Int(readLine()!)!

var result = 0

for i in 1...N {
  let nums = String(i).map { Int(String($0))! }

  if i + nums.reduce(0, +) == N {
    result = i
    break
  }
}

print("\(result)")
