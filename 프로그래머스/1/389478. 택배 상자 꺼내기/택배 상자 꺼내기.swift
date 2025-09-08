import Foundation

func solution(_ n:Int, _ w:Int, _ num:Int) -> Int {
    
    let dir = [(0, 1), (1, 0), (0, -1), (1, 0)]
    var dirIndex = 0
    
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
    
    var row = 0
    var col = 0
    for number in 1...n {
        board[row][col] = number
        
        if number == num { targetIndex = (row, col) }
        
        var (r, c) = dir[dirIndex]
        var nextR = row + r
        var nextC = col + c
        
        if nextC < 0 || nextC >= w {
            dirIndex = (dirIndex + 1) % 4
            (r, c) = dir[dirIndex]
            nextR = row + r
            nextC = col + c
            dirIndex = (dirIndex + 1) % 4
        }
        
        row = nextR
        col = nextC
    }
    
    while targetIndex.0 < board.count {
        let row = targetIndex.0
        let col = targetIndex.1
        targetIndex = (row + 1, col)
        if board[row][col] != 0 { result += 1 }
    }
    
    return result
    
}