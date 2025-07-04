import Foundation

func solution(_ board:[[Int]]) -> Int {
    var board = board
    let dir = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    var result = 0
    
    for row in 0..<board.count {
        for col in 0..<board.count {
            if board[row][col] != 1 { continue }
            
            for d in dir {
                let nextRow = row + d.0
                let nextCol = col + d.1
                
                if nextRow >= 0 && nextRow < board.count && nextCol >= 0 && nextCol < board.count {
                    if board[nextRow][nextCol] != 1 {
                        board[nextRow][nextCol] = 2
                    }
                }
            }
        }
    }
    
    for row in 0..<board.count {
        for col in 0..<board.count {
            if board[row][col] == 0 { result += 1 }
        }
    }
    
    return result
}

