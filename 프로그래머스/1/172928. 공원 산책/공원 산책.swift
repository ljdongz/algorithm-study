import Foundation

func solution(_ park:[String], _ routes:[String]) -> [Int] {
    
    let direction: [String: (Int, Int)] = [
        "E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)
    ]
    
    var board: [[String]] = []
    var curIndex: (Int, Int) = (0, 0)
    
    for pk in park {
        let p = pk.map { String($0) }
        board.append(p)
        
        let row = board.count - 1
        for col in 0..<board[row].count {
            if board[row][col] == "S" { curIndex = (row, col) }
        }
    }
    
    out: for route in routes {
        
        var index = curIndex
        
        let r = route.split(separator: " ").map { String($0) }
        let dir = direction[r[0]]!
        let count = Int(r[1])!
        
        for _ in 0..<count {
            let nextR = index.0 + dir.0
            let nextC = index.1 + dir.1
            
            if nextR < 0 || nextR >= board.count || nextC < 0 || nextC >= board[0].count { continue out }
            if board[nextR][nextC] == "X" { continue out }
            
            index = (nextR, nextC)
        }
        
        curIndex = index
    }
    
    
    return [curIndex.0, curIndex.1]
}