import Foundation

/*

1. 에너지 구슬 하나를 고른다. 고른 에너지 구슬의 번호를 x라고 한다. 
    단, 첫 번째와 마지막 에너지 구슬은 고를 수 없다.
2. x번째 에너지 구슬을 제거한다.
3. Wx-1 × Wx+1의 에너지를 모을 수 있다.
4. N을 1 감소시키고, 에너지 구슬을 1번부터 N번까지로 다시 번호를 매긴다. 
    번호는 첫 구슬이 1번, 다음 구슬이 2번, ... 과 같이 매겨야 한다.

*/

let n = Int(readLine()!)!
let energies = readLine()!.split(separator: " ").map { Int(String($0))! }
var result = 0


func recursive(sum: Int, curr: [Int]) {
  if curr.count == 2 {
    result = max(result, sum)
    return
  }

  for i in 1..<curr.count - 1 {
    var curr = curr
    let s = curr[i-1] * curr[i+1]
    curr.remove(at: i)
    recursive(sum: sum + s, curr: curr)
  }
}

recursive(sum: 0, curr: energies)
print(result)