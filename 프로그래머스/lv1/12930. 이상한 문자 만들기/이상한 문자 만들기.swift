import Foundation

func solution(_ s:String) -> String {
    var str = Array(s)
    var index = 0
    var result = ""
    
    for s in str {
        if s == " " {
            result += " "
            index = 0
        } else if index % 2 == 0 {
            result += s.uppercased()
            index += 1
        } else {
            result += s.lowercased()
            index += 1
        }
        
    }
    
    return result
}
