import Foundation

let n = Int(readLine()!)!

var dic: [String: Int] = [:]

for _ in 0..<n {
  let ext = String(readLine()!.split(separator: ".").last!)
  dic[ext, default: 0] += 1
}

let arr = dic.sorted { $0.key < $1.key }
arr.forEach { print($0.key, $0.value) }