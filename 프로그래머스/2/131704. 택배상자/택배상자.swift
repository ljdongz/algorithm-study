import Foundation

func solution(_ order:[Int]) -> Int {
    
    var result = 0
    
    var mainStack: [Int] = order.reversed()
    var subStack: [Int] = []
    
    for i in 1...order.count {
        if mainStack.last == i {
            result += 1
            mainStack.removeLast()
            
            while !mainStack.isEmpty && subStack.last == mainStack.last {
                result += 1
                mainStack.removeLast()
                subStack.removeLast()
            }
            
        } else if subStack.last == i {
            result += 1
            subStack.removeLast()
            
            while !mainStack.isEmpty && subStack.last == mainStack.last {
                result += 1
                mainStack.removeLast()
                subStack.removeLast()
            }
        } else {
            subStack.append(i)
        }
    }
    
    return result
}
