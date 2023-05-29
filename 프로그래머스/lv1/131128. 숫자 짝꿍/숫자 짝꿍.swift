import Foundation
func solution(_ X:String, _ Y:String) -> String {
    var xArray: [Int] = Array(repeating: 0, count: 10)
    var yArray: [Int] = Array(repeating: 0, count: 10)
    var result: String = ""
    
    for n in X {
        xArray[Int(String(n))!] += 1
    }
    for n in Y {
        yArray[Int(String(n))!] += 1
    }
    
    for i in (0...9) {
        result += String(repeating: String(i), count: min(xArray[i], yArray[i]))
    }
    
    result = String(result.sorted(by: >))
    
    if result.isEmpty {
        return "-1"
    } else if String(result.first!) == "0" {
        return "0"
    } else {
        return result
    }
    
}
