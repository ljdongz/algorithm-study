import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    
    func recursive(index: Int, sum: Int) -> Int {
        if index == numbers.count {
            return target == sum ? 1 : 0
        }
        
        let left = recursive(index: index + 1, sum: sum + numbers[index])
        let right = recursive(index: index + 1, sum: sum - numbers[index])
        
        return left + right
    }
    
    return recursive(index: 0, sum: 0)
}