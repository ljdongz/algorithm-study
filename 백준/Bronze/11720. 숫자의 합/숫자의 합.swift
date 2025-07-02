import Foundation

let N = Int(readLine()!)!

let num = readLine()!.map { Int(String($0))! }.reduce(0) { $0 + $1 }

print(num)