func solution(_ cacheSize:Int, _ cities:[String]) -> Int {

    var cache: [String] = []
    var result = 0
    
    for city in cities {
        var newCache: [String] = []
        
        var hit = ""
        for ch in cache {
            if ch == city.lowercased() { 
                hit = ch
                continue
            }
            
            newCache.append(ch)
        }
        
        if !hit.isEmpty { 
            newCache.append(hit) 
            result += 1
        } else {
            if cacheSize != 0 {
                if newCache.count >= cacheSize {
                newCache.removeFirst()
                }
                newCache.append(city.lowercased())    
            }
            
            result += 5
        }
        cache = newCache
        
    }
    
    return result
}
