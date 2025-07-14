import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

let x = input[0]
let y = input[1]
let p1 = input[2]
let p2 = input[3]

var currentX = p1
var currentY = p2
while currentX <= 10100 && currentY <= 10100 {

  if currentX == currentY {
    break
  }

  if currentX > currentY {
    currentY += y
  } else {
    currentX += x
  }
}

if currentX <= 10100 && currentY <= 10100 {
  print(currentX)
} else {
  print(-1)
}