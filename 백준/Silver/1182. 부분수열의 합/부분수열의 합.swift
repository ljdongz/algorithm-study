import Foundation

// 1) N개의 원소 중 M개를 뽑아서 만들 수 있는 조합을 구한다
// 2) 1에서 만든 조합의 합을 구해서 S와 동일한지 비교한다
// 3) 1...N개까지 1~2를 반복한다

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let target = input[1]

let numbers = readLine()!.split(separator: " ").map { Int(String($0))! }
var result = 0

func recursive(k: Int, sum: Int, used: Int) {
  if k == n {
    if used == 0 { return }
    if sum == target { result += 1 }
    return 
  }

  recursive(k: k + 1, sum: sum + numbers[k], used: used + 1) // 지금 바라보는 박스를 선택하는 경우
  recursive(k: k + 1, sum: sum, used: used) // 지금 바라보는 박스를 선택하지 않는 경우
}

/*
순서
O O O O
O O O X
O O X O
O O X X
...
*/

recursive(k: 0, sum: 0, used: 0)

print(result)