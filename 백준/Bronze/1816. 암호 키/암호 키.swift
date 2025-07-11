import Foundation

let N = Int(readLine()!)!

loop: for _ in 0..<N {
  let S = Int(readLine()!)!

  for i in 2...1000000 {
    if S % i == 0 {
      print("NO")
      continue loop
    }
  }

  print("YES")
}

