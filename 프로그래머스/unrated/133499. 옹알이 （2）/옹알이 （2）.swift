import Foundation
func solution(_ babbling:[String]) -> Int {
    
    var result = 0
    var words = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling {
        var b = bab
        b = b.replacingOccurrences(of: "aya", with: "1")
        b = b.replacingOccurrences(of: "ye", with: "2")
        b = b.replacingOccurrences(of: "woo", with: "3")
        b = b.replacingOccurrences(of: "ma", with: "4")
        if Int(b) != nil && !b.contains("11") && !b.contains("22") && !b.contains("33") && !b.contains("44") { result += 1 }
    }
    return result
}