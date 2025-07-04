import Foundation

func solution(_ n:Int) -> [[Int]] {
    var array: [[Int]] = Array(
        repeating: Array(
            repeating: 0, 
            count: n
        ), 
        count: n
    )
    let direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    var dIndex = 0
    
    var row = 0
    var col = 0
    var index = 1
    
    
    while array[row][col] == 0 {
        
        array[row][col] = index
        
        index += 1
        
        let (r, c) = direction[dIndex]
        let nextRow = row + r
        let nextCol = col + c
        if nextRow < 0 || nextRow >= n || nextCol < 0 || nextCol >= n || array[nextRow][nextCol] != 0 {
            dIndex = (dIndex + 1) % 4
            let (r1, c1) = direction[dIndex]
            row += r1
            col += c1
        } else {
            row += r
            col += c
        }
        
        if row < 0 || row >= n || col < 0 || col >= n { break }
    }
    
    return array
}