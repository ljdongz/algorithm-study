import Foundation

func solution(_ players:[Int], _ m:Int, _ k:Int) -> Int {
    
    var exitTime: [Int] = .init(repeating: 0, count: 1024)
    var serverCount = 0
    var result = 0
    
    for time in 0..<players.count {
        serverCount -= exitTime[time]
        
        let totalServer = (players[time] / m)
        
        if serverCount < totalServer {
            exitTime[time + k] = totalServer - serverCount
            result += totalServer - serverCount
            serverCount = totalServer
        }
    }
    
    return result
}