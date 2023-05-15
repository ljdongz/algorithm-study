import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    
    if (d.reduce(0, +) <= budget) { return d.count }
    
    var a = d.sorted()
    var result = 0
    
    for int in a {
        result += int
        if result > budget {
            break
        }
        a.removeFirst()
    }
    
    return d.count - a.count
}
