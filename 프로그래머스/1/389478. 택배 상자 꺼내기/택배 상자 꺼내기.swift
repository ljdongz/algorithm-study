import Foundation

func solution(_ n:Int, _ w:Int, _ num:Int) -> Int {
    
    let rowCount = (n / w) + (n % w == 0 ? 0 : 1)
    var board: [[Int]] = .init(
        repeating: .init(
            repeating: 0,
            count: w
        ),
        count: rowCount
    )
    var targetIndex = (0, 0)
    var result = 0
    
    var number = 1
    out: for row in 0..<board.count {
        
        let isForward = row % 2 == 0
        
        for col in 0..<w {
            if number > n { break out }
            
            let r = row
            let c = isForward ? col : (w - col - 1)
            
            board[r][c] = number
            
            if number == num { targetIndex = (r, c) }
            
            number += 1
        }
    }
 
    while targetIndex.0 < board.count {
        let row = targetIndex.0
        let col = targetIndex.1
        if board[row][col] != 0 { result += 1 }
        targetIndex = (row + 1, col)
    }
    
    return result
}