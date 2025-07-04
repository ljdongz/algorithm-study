import Foundation

func solution(_ polynomial: String) -> String {
    let poly = polynomial.split(separator: " ").joined().split(separator: "+").map { String($0) }
    
    var xNumber = 0
    var number = 0
    var result = ""
    
    for p in poly {
        if p.contains("x") {
            let a = p.split(separator: "x")
            
            xNumber += a.isEmpty ? 1 : Int(a[0])!
        } else {
            number += Int(p)!
        }
    }
    
    if xNumber > 1 {
        result += "\(xNumber)x"
    } else if xNumber == 1 {
        result += "x"
    }
    
    if number != 0 {
        if result.isEmpty {
            result += "\(number)"
        } else {
            result += " + \(number)"    
        }
    }
    
    return result
}