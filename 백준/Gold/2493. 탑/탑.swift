import Foundation

let n = Int(readLine()!)!

var result = ""

var stack: [(height: Int, pos: Int)] = []

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

for i in 0..<input.count {
  
  let value = (height: input[i], pos: i+1)

  while let last = stack.last {

    if last.height >= value.height {
      result += "\(last.pos) "
      stack.append(value)
      break
    } else {
      _ = stack.popLast()
    }
  }

  if stack.isEmpty { 
    result += "0 " 
    stack.append(value)
  }
}


print(result)