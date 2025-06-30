import Foundation

func solution(_ babbling:[String]) -> Int {
    let words = ["aya", "ye", "woo", "ma"]
    var count = 0
    
    
    for bab in babbling {
        var bab = bab
        
        for word in words {
            let split = bab.components(separatedBy: word).joined(separator: " ")
            bab = split
        }
        
        if bab.trimmingCharacters(in: .whitespaces).isEmpty { 
            count += 1
            continue
        }
    }
    
    return count
}