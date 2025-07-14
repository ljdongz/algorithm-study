import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

var rooms: [[Int]] = []
let total = input[3]

for i in 0..<3 {
  let room = input[i]

  var possible: [Int] = []
  var current = 0

  while current <= total {
    possible.append(current)
    current += room
  }

  rooms.append(possible)
}

var flag = 0
out: for i in rooms[0] {
  for j in rooms[1] {
    for k in rooms[2] {
      if i + j + k == total {
        flag = 1
        break out
      }
    }
  }
}
print(flag)