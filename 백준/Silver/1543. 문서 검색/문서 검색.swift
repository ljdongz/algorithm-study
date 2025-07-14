import Foundation

let document = readLine()!
let word = readLine()!

let components = document.components(separatedBy: word).filter { $0 != "" }.joined(separator: "")
print((document.count - components.count) / word.count)