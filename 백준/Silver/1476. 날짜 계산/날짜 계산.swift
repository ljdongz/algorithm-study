import Foundation

/*
E : 지구  1 <= E <= 15
S : 태양  1 <= S <= 28
M : 달   1 <= M <= 19
*/

let input = readLine()!.split(separator: " ").map { Int($0)! }

var year = 0

while true {
  let e = year % 15 + 1
  let s = year % 28 + 1
  let m = year % 19 + 1

  if (e, s, m) == (input[0], input[1], input[2]) {
    print(year + 1)
    break
  }

  year += 1
}