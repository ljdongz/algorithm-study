import Foundation

let n = Int(readLine()!)!
let target = readLine()!.split(separator: " ").map { Int(String($0))! }
var recipies: [[Int]] = []
for _ in 0..<n {
  recipies.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

var price = Int.max // 비용
var numbers: [Int] = [] // 식재료 번호

// curPrice: 현재 식재료 비용
// curNums: 현재 식재료 번호
// curValue: 현재 식재료 영양성분
// start: 시작 인덱스
func recursive(curPrice: Int, curNums: [Int], curValue: [Int], start: Int) {
  if !curNums.isEmpty {
    if curValue[0] >= target[0] && curValue[1] >= target[1] && curValue[2] >= target[2] && curValue[3] >= target[3] {
      if price > curPrice {
        price = curPrice
        numbers = curNums
      }
      return
    }
  }

  for i in start..<n {
    let recipe = recipies[i]
    var nums = curNums
    nums.append(i + 1)
    let value = [curValue[0] + recipe[0], curValue[1] + recipe[1], curValue[2] + recipe[2], curValue[3] + recipe[3]]

    recursive(
      curPrice: curPrice + recipe[4],
      curNums: nums,
      curValue: value,
      start: i + 1
    )
  }
}

recursive(curPrice: 0, curNums: [], curValue: [0, 0, 0, 0], start: 0)

if numbers.isEmpty {
  print(-1)
} else {
  print(price)

  for num in numbers {
    print(num, terminator: " ")
  }
}
