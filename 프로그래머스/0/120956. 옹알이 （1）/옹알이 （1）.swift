import Foundation

/*



*/

func solution(_ babbling:[String]) -> Int {
    let words = ["aya", "ye", "woo", "ma"]
    var count = 0
    
    var combines: [String] = []
    
    for i in 1...4 {
        
        for x in 0..<words.count {
            
            for y in 0..<words.count {
                if i == 1 || x == y { continue }
                
                for z in 0..<words.count {
                    if i == 2 || x == z || y == z { continue }
                    
                    for w in 0..<words.count {
                        if i == 3 || x == w || y == w || z == w { continue }
                        
                        combines.append(words[x] + words[y] + words[z] + words[w])
                    }
                    
                    combines.append(words[x] + words[y] + words[z])
                }
                
                combines.append(words[x] + words[y])
            }
            
            combines.append(words[x])
        }
    }
    
    for bab in babbling {
        if combines.contains(bab) { count += 1 }
    }
    
    return count
}