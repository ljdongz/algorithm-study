import Foundation

// 1) N개의 원소 중 M개를 뽑아서 만들 수 있는 조합을 구한다
// 2) 1에서 만든 조합의 합을 구해서 S와 동일한지 비교한다
// 3) 1...N개까지 1~2를 반복한다

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let target = input[1]

let numbers = readLine()!.split(separator: " ").map { Int(String($0))! }
var result = 0

// k: 현재까지 뽑은 숫자 개수
// s: 시작점
// m: 뽑아야 하는 숫자 개수
// sum: 현재까지 합
func recursive(k: Int, s: Int, m: Int, sum: Int) {
  if k == m {
    if sum == target { result += 1 }
    return
  }

  for i in s..<n {
    recursive(k: k + 1, s: i + 1, m: m, sum: sum + numbers[i])
  }
}

for i in 1...n {
  recursive(k: 0, s: 0, m: i, sum: 0)
}

print(result)