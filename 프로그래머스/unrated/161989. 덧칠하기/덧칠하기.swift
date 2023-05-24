import Foundation

func solution(_ n:Int, _ m:Int, _ section:[Int]) -> Int {
    
    var result = 0
    var paintArrange = 0
    
    for i in (0..<section.count) {
        if paintArrange >= section[i] { continue }
        paintArrange = section[i] + m - 1
        result += 1
    }
    return result
}