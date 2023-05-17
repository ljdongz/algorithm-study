import Foundation
func solution(_ food:[Int]) -> String {
    var result = ""
    for i in 1..<food.count {
        result += String(repeating: "\(i)", count: food[i] / 2)
    }
    return result + "0" + result.reversed()
}