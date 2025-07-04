import Foundation

func solution(_ dots:[[Int]]) -> Int {
    
    let sortedDots = dots.sorted { ($0[0], $0[1]) < ($1[0], $1[1]) }
    
    let x = sortedDots[0]
    let y = sortedDots[3]
    
    
    
    return (y[0] - x[0]) * (y[1] - x[1])
}