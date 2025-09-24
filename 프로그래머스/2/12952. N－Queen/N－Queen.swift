import Foundation

func solution(_ n:Int) -> Int {
    
    var ignored = Array(repeating: Array(repeating: false, count: n), count: n)
    
    func recursive(row: Int, ignored: [[Bool]]) -> Int {
        
        if row >= n { return 1 }
        
        var count = 0
        
        for col in 0..<n {
            var ignored = ignored
            
            if ignored[row][col] { continue }

            ignored[row][col] = true

            var lCount = 1
            while true {
                if row + lCount < n && col - lCount >= 0 {
                    ignored[row + lCount][col - lCount] = true
                    lCount += 1
                } else {
                    break
                }
            }

            var rCount = 1
            while true {
                if row + rCount < n && col + rCount < n {
                    ignored[row + rCount][col + rCount] = true
                    rCount += 1
                } else {
                    break
                }
            }
            
            var rowCount = 1
            while true {
                if row + rowCount < n {
                    ignored[row + rowCount][col] = true
                    rowCount += 1
                } else {
                    break
                }
            }

            count += recursive(row: row + 1, ignored: ignored)
            
        }
        
        return count
    }
    
    return recursive(row: 0, ignored: ignored)
}




