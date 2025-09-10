import Foundation

func solution(_ expression:String) -> Int64 {
    
    let opss = [
        ["+", "-", "*"], ["+", "*", "-"],
        ["-", "+", "*"], ["-", "*", "+"],
        ["*", "-", "+"], ["*", "+", "-"],
    ]
    
    var maximum = 0
    
    for ops in opss {
        
        let result = recursive(expression: expression, ops: ops, index: 0)
        
        maximum = max(maximum, abs(result))
    }
    
    return Int64(maximum)
}

func recursive(expression: String, ops: [String], index: Int) -> Int {
    if index >= ops.count  { return 0 }
    
    let op = ops[index]    
    let split = expression.split(separator: Character(op)).map { String($0) }
    
    var result: Int? = nil
    
    for exp in split {
        // 연산자가 없는 경우 (정수로만 이루어진 경우)
        if let value = Int(exp) {
            if let res = result {
                if op == "+" { result = res + value }
                else if op == "-" { result = res - value }
                else if op == "*" { result = res * value }
            } else {
                result = value
            }
        } else {
            let value = recursive(expression: exp, ops: ops, index: index + 1)
            if let res = result {
                if op == "+" { result = res + value }
                else if op == "-" { result = res - value }
                else if op == "*" { result = res * value }
            } else {
                result = value
            }
        }
    }
    
    return result!
}