import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var result: [Int] = []
    var topScore: [Int] = []
    
    score.forEach {
        topScore.append($0)
        topScore = Array(topScore.sorted().reversed().prefix(k))
        result.append(topScore.last!)
    }
    
    return result
}