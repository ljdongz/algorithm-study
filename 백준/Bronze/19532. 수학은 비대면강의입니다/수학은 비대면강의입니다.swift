import Foundation

/*
(a-d)x + (b-e)y = c-f
*/

let input = readLine()!.split(separator: " ").map { Int($0)! }

let a = input[0]
let b = input[1]
let c = input[2]
let d = input[3]
let e = input[4]
let f = input[5]

out: for x in -999...999 {
  for y in -999...999 {
    let first = (a * x) + (b * y) == c
    let second = (d * x) + (e * y) == f

    if first && second {
      print(x, y)
      break out
    }
  }
}