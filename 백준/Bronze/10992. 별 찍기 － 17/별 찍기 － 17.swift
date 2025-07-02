import Foundation

let N = Int(readLine()!)!

var result = ""

if N == 1 { print("*") }
else if N == 2 { 
  print(
    """
     *
    ***
    """
  )
}
else {
  for row in 1...(N-1) {
    for col in 1...(N + row - 1) {
      if N + row - 1 < col { continue }

      if N - row + 1 == col || N + row - 1 == col {
        result += "*"
      } else {
        result += " "
      }
    }
    result += "\n"
  }

  for _ in 1...(N * 2 - 1) {
    result += "*"
  }

  print(result)
}