import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    var sortedScore = score.sorted(by: >)
    
    return stride(from: m-1, to: score.count, by: m).reduce(0, {
        $0 + (m * sortedScore[$1])
    })
}