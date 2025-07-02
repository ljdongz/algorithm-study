import Foundation

let N = Int(readLine()!)!

var result = ""

for i in stride(from: N, to: 0, by: -1) {

  var count = 0
  var flag = true
  
  for j in 1...(N * 2 - 1) {
    if j < i { 
      result += " " 
      continue
    }

    if count == N - i + 1 { continue }

    if flag { 
      result += "*"
      count += 1
    } else {
      result += " "
    }
    flag.toggle()
  }

  if i != 1 { result += "\n" }
}

print(result)
