import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    
    func recursive(cur: Int, index: Int) -> Int {
        if index >= numbers.count {
            return cur == target ? 1 : 0
        }
        
        let plus = recursive(
            cur: cur + numbers[index],
            index: index + 1
        )
        let minus = recursive(
            cur: cur - numbers[index],
            index: index + 1
        )
        
        return plus + minus
    }
    
    return recursive(cur: 0, index: 0)
}