import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    
    var reportDict: [String: Set<String>] = [:]
    var receiveDict: [String: Int] = [:]
    var result: [Int] = []
    
    for rep in report {
        let split = rep.split(separator: " ").map { String($0) }
        let from = split[0]
        let to = split[1]
        
        var list = reportDict[to] ?? Set<String>()
        list.insert(from)
        reportDict[to] = list
    }
    
    for (from, list) in reportDict {
        if list.count < k { continue }
        
        for to in list {
            receiveDict[to] = (receiveDict[to] ?? 0) + 1
        }
    }
    
    for id in id_list {
        result.append(receiveDict[id] ?? 0)
    }
    
    return result
}