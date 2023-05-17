import Foundation
func solution(_ food:[Int]) -> String {
    var arr: [String] = ["0"]
    for i in (1..<food.count).reversed() {
        arr.insert((String(repeating: "\(i)", count: food[i]/2)), at: 0)
        arr.append(String(repeating: "\(i)", count: food[i]/2))
    }
    
    return arr.reduce("", +)
}
