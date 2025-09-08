import Foundation

func solution(_ n:Int, _ edge:[[Int]]) -> Int {
    
    var visited: [Int] = .init(repeating: -1, count: n + 1)
    var board: [[Int]] = .init(
        repeating: [],
        count: n + 1
    )
    
    for e in edge {
        board[e[0]].append(e[1])
        board[e[1]].append(e[0])
    }
    
    var queue: [Int] = [1]
    visited[1] = 0
    var front = 0
    var maximum = 0
    
    while queue.count >= front + 1 {
        let curNode = queue[front]
        front += 1
        let curDist = visited[curNode]
        maximum = max(maximum, curDist)
        
        for nextNode in board[curNode] {
            if visited[nextNode] == -1 { 
                queue.append(nextNode)
                visited[nextNode] = curDist + 1
            }    
        }
    }
    
    return visited.filter { $0 == maximum }.count
    
}