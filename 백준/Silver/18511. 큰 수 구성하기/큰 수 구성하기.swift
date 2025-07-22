import Foundation

let input = readLine()!.split(separator: " ").map { String($0) }
let n = input[0]
let k = Int(input[1])!

let nums = readLine()!.split(separator: " ").map { String($0) }.sorted { $0 > $1 }
var flag = false
var result = ""

func recursive(targetLength: Int, curLength: Int, curNum: String) {
  if curLength == targetLength {
    if Int(curNum)! <= Int(n)! {
      flag = true
      result = curNum
    }

    return
  }

  for i in 0..<k {
    if flag { break }
    recursive(targetLength: targetLength, curLength: curLength + 1, curNum: curNum + nums[i])
  }
}

for i in stride(from: n.count, to: n.count - 2, by: -1) {
  if flag { break }
  recursive(targetLength: i, curLength: 0, curNum: "")
}

print(result)