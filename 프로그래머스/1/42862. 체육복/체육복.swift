import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var students: [Int] = Array(repeating: 1, count: n)
    
    for i in 0..<lost.count {
        students[lost[i]-1] -= 1
    }
    
    for i in 0..<reserve.count {
        students[reserve[i]-1] += 1
    }
    
    print(students)
    
    for i in 0..<students.count {
        if students[i] != 2 { continue }

        if i-1 >= 0 && students[i-1] == 0 {
            students[i] -= 1
            students[i-1] += 1
            continue
        }

        if i+1 < students.count && students[i+1] == 0 {
            students[i] -= 1
            students[i+1] += 1
        }
    }
    
    return students.filter({ $0 >= 1 }).count
}