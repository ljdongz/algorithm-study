import Foundation

func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    var result: [Int] = []
    
    for i in 0..<photo.count {
        var sum = 0
        for j in 0..<name.count {
            if photo[i].contains(name[j]) { sum += yearning[j] }
        }
        result.append(sum)
    }
    
    return result
}