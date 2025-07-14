import Foundation

let document = readLine()!
let word = readLine()!

let components = document.components(separatedBy: word).joined(separator: "")
print((document.count - components.count) / word.count)