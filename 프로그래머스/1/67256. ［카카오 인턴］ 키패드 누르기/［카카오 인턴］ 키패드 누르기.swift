import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    
    var keypad: [Int: (Int, Int)] = [0: (3, 1)]
    let leftKey = Set([1, 4, 7])
    let rightKey = Set([3, 6, 9])
    for row in 0..<3 {
        for col in 0..<3 {
            keypad[(row * 3 + col + 1)] = (row, col)
        }
    }
    
    var leftIndex = (3, 0)
    var rightIndex = (3, 2)
    var result = ""
    
    for num in numbers {
        
        if leftKey.contains(num) {
            result += "L"
            leftIndex = keypad[num]!
        } else if rightKey.contains(num) {
            result += "R"
            rightIndex = keypad[num]!
        } else {
            let target = keypad[num]!
            let lDist = abs(target.0 - leftIndex.0) + abs(target.1 - leftIndex.1)
            let rDist = abs(target.0 - rightIndex.0) + abs(target.1 - rightIndex.1)
            
            if lDist < rDist {
                result += "L"
                leftIndex = target
            } else if lDist > rDist {
                result += "R"
                rightIndex = target
            } else {
                if hand == "left" {
                    result += "L"
                    leftIndex = target
                } else {
                    result += "R"
                    rightIndex = target
                }
            }
        }
    }
    
    return result
}