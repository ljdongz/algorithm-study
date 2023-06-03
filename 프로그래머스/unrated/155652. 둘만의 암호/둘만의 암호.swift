import Foundation

func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    var str = Array("abcdefghijklmnopqrstuvwxyz".filter({ !skip.contains($0) }))
    var result = ""
    
    for c in s {
        var idx = str.firstIndex(of: c)! + index
        result += (idx >= str.count) ? String(str[idx % str.count]) : String(str[idx])
    }
    
    return result
}