import Foundation

func solution(_ answers:[Int]) -> [Int] {
    var a = [1,2,3,4,5]
    var b = [2,1,2,3,2,4,2,5]
    var c = [3,3,1,1,2,2,4,4,5,5]
    
    var count = [0, 0, 0]
    var result: [Int] = []
    
    for i in 0..<answers.count {
        if answers[i] == a[i % 5] { count[0] += 1 }
        if answers[i] == b[i % 8] { count[1] += 1 }
        if answers[i] == c[i % 10] { count[2] += 1 }
    }
    
    for i in 0..<count.count {
        if count[i] == count.max()! { result.append(i+1) }
    }
    
    return result
}