import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var zeroCount = lottos.filter({ $0 == 0 }).count
    var winCount = lottos.filter({ win_nums.contains($0) }).count
    
    return [min(7-zeroCount-winCount, 6), min(7-winCount, 6)]
}