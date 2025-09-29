import Foundation

func solution(_ X:String, _ Y:String) -> String {
    var xArray = Array(repeating: 0, count: 10)
    var yArray = Array(repeating: 0, count: 10)
    
    var result = ""
    
    X.map { Int(String($0))! }.forEach { xArray[$0] += 1 }
    Y.map { Int(String($0))! }.forEach { yArray[$0] += 1 }
    
    for i in stride(from: 9, to: -1, by: -1) {
        
        let count = min(xArray[i], yArray[i])
        
        for _ in 0..<count {
            result += "\(i)"
        }
    }
    
    if result.isEmpty { return "-1" }
    else if result.first == "0" { return "0" }
    else { return result }
}
