import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var result = 0
    var basket: [Int] = []
    var boards = board
    
    for pos in moves {
        for idx in boards.indices {
            if boards[idx][pos-1] == 0 { continue }
            
            basket.append(boards[idx][pos-1])
            boards[idx][pos-1] = 0
            break
        }
        
        while(basket.count > 1) {
            if basket[basket.count - 1] != basket[basket.count - 2] { break }
            basket = Array(basket.prefix(basket.count - 2))
            result += 2
        }
    }
    
    return result
}