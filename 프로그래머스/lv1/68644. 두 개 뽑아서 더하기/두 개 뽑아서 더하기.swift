import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var result: Set<Int> = []
    for i in 0..<numbers.count - 1 {
        for j in i+1..<numbers.count {
            result.insert(numbers[i] + numbers[j])
        }
    }
    return [Int](result.sorted())
}