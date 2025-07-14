import Foundation

let N = Int(readLine()!)!

var result = [0, 0]
var current = [0, 0]

var trophys: [Int] = []
for _ in 0..<N {
  trophys.append(Int(readLine()!)!)
}


for i in 0..<trophys.count {
  if current[0] < trophys[i] {
    result[0] += 1
    current[0] = trophys[i]
  }

  if current[1] < trophys[trophys.count - 1 - i] {
    result[1] += 1
    current[1] = trophys[trophys.count - 1 - i]
  }
}

print(result[0])
print(result[1])

