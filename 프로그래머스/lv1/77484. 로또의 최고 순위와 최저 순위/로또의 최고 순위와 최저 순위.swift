import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var zeroCount = 0
    var correct = 0
    for num in lottos {
        if num == 0 {
            zeroCount += 1
            continue
        }
        if win_nums.contains(num) { correct += 1 }
    }
    return [7-max(min(correct + zeroCount, 6), 1), 7-max(correct, 1)]
}