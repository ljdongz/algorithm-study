import Foundation

func solution(_ babbling:[String]) -> Int {
    
    var result = 0
    var words = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling {
        var b = bab
        for word in words {
            b = b.replacingOccurrences(of: word, with: " ")
        }
        b = b.replacingOccurrences(of: " ", with: "")
        if b.isEmpty && !bab.contains("ayaaya") && !bab.contains("yeye") && !bab.contains("woowoo") && !bab.contains("mama") { result += 1 }
    }
    
    return result
}