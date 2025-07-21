import Foundation

// 1) N개의 원소 중 M개를 뽑아서 만들 수 있는 조합을 구한다
// 2) 1에서 만든 조합의 합을 구해서 S와 동일한지 비교한다
// 3) 1...N개까지 1~2를 반복한다

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let target = input[1]

let numbers = readLine()!.split(separator: " ").map { Int(String($0))! }
var result = 0

// total: 뽑아야 하는 숫자 개수
// cur: 현재까지 뽑은 숫자 개수
// start: 시작점
// sum: 현재까지 합
func recursive(total: Int, cur: Int, start: Int, sum: Int) {
  if cur == total {
    if sum == target { result += 1 }
    return
  }

  for i in start..<n {
    recursive(total: total, cur: cur + 1, start: i + 1, sum: sum + numbers[i])
  }
}

for i in 1...n {
  recursive(total: i, cur: 0, start: 0, sum: 0)
}

print(result)