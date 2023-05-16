import Foundation

func solution(_ t:String, _ p:String) -> Int {
    
    var array = Array(t)
    var str = ""
    var result = 0
    
    for i in 0..<t.count - p.count + 1 {
        for j in 0..<p.count {
            str += String(array[i+j])
        }
        if Int(str)! <= Int(p)! { result += 1 }
        str = ""
    }
    
    
    return result
}