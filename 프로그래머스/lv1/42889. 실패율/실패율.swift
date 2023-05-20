import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var currentUser = 0
    var stageRate: [Int: Double] = [:]
    var userCount: [Int] = Array(repeating: 0, count: N+1)
    
    for i in stages {
        userCount[i-1] += 1
    }

    for i in 1...N {
        let rate = Double(userCount[i-1]) / Double(stages.count - currentUser)
        stageRate[i] = rate.isNaN ? 0.0 : rate
        currentUser += userCount[i-1]
    }

    return stageRate.sorted { $0.value == $1.value ? $0.key < $1.key : $0.value > $1.value }.compactMap({$0.key})
}
