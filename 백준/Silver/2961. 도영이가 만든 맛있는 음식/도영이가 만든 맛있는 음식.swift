import Foundation

/*
N: 재료의 개수
S: 신맛
B: 쓴맛

음식의 신맛: 각 재료의 신맛을 곱한 값
음식의 쓴맛: 각 재료의 쓴맛을 더한 값

요리의 신맛과 쓴맛의 차이를 적게
*/

let n = Int(readLine()!)!
var receipt: [[Int]] = []
var result = Int.max

for _ in 0..<n { 
  let input = readLine()!.split(separator: " ").map { Int(String($0))! }
  receipt.append(input)
}

func recursive(total: Int, cur: Int, start: Int, sum: Int, mul: Int) {
  if cur == total {
    result = min(result, abs(sum - mul))
    return
  }

  for i in start..<n {
    let mul = mul * receipt[i][0]
    let sum = sum + receipt[i][1]
    recursive(total: total, cur: cur + 1, start: i + 1, sum: sum, mul: mul)
  }
}

for i in 1...n {
  recursive(total: i, cur: 0, start: 0, sum: 0, mul: 1)
}

print(result)


