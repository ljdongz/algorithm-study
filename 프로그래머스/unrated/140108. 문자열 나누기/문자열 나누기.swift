import Foundation

func solution(_ s:String) -> Int {

    var firstStr = ""
    var firstCount = 0
    var diffCount = 0
    var result = 0
    
    for c in s {
        if firstStr == "" { 
            firstStr = String(c)
        }
        
        if firstStr == String(c) { firstCount += 1 }
        else { diffCount += 1 }
        
        if firstCount == diffCount {
            firstStr = ""
            result += 1
            firstCount = 0
            diffCount = 0
        }
    }
    
    if firstStr != "" { result += 1 }
    
    return result
}