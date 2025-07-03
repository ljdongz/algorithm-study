import Foundation

let chess = [1, 1, 2, 2, 2, 8]

let numbers = readLine()!.split(separator: " ").map { Int(String($0))! }

var result = ""

for i in 0..<numbers.count {
    result += "\(chess[i] - numbers[i])"
    
    if i != numbers.count - 1 {
        result += " "
    }
}

print(result)