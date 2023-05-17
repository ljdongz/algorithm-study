import Foundation

func solution(_ s:String) -> [Int] {
    var str = Array(s)
    var result: [Int] = []
    
    for i in (0..<s.count) {
        for j in (0..<i).reversed() {
            if result.count != i { continue }
            if str[i] == str[j] { result.append(i-j) }
        }
        if result.count == i { result.append(-1) }
    }
    return result
}