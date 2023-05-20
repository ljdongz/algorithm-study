import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    var result = 0
    var reminder = 0
    var sortedScore = score.sorted(by: {$0 > $1})
    
    for i in (1...k).reversed() {
        var a = sortedScore.filter({$0 == i})
        if (a.count + reminder) >= m {
            result += (i * m * ((a.count + reminder) / m))
        }
        reminder = (a.count + reminder) % m
    }
    
    return result
}