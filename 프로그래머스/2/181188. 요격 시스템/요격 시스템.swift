import Foundation

/*
1. 끝 점(e)을 기준으로 정렬
2. 
*/

func solution(_ targets:[[Int]]) -> Int {
    
    let sortedTarget = targets.sorted { $0[1] < $1[1] }
    
    var temp = 0
    var answer = 0
    for target in sortedTarget {
        if target[0] >= temp {
            temp = target[1]
            answer += 1
        }
    }
    
    return answer
}