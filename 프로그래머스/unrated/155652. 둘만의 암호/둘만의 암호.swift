import Foundation

func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    var result = ""
    for c in s {
        var asc = UnicodeScalar(String(c))!.value
        for _ in 1...index {
            asc += 1
            if asc == 123 { asc = 97 } 
            while(skip.contains(String(UnicodeScalar(asc)!))) {
                asc += 1
                if asc == 123 { asc = 97 } 
            }
            if asc == 123 { asc = 97 } 
        }
        result += String(UnicodeScalar(asc)!)
    }
    
    return result
}