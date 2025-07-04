import Foundation

let N = Int(readLine()!)!

var array: [(String, Int, Int, Int)] = []

for _ in 0..<N {
  let input = readLine()!.split(separator: " ")
  let data = (String(input[0]), Int(input[1])!, Int(input[2])!, Int(input[3])!)
  array.append(data)
}

array.sort { 
  if $0.1 == $1.1 {
    if $0.2 == $1.2 {
      if $0.3 == $1.3 {
        return $0.0 < $1.0
      } else {
        return $0.3 > $1.3
      }
    } else {
      return $0.2 < $1.2
    }
  } else {
    return $0.1 > $1.1
  }
}

array.forEach { print($0.0) }