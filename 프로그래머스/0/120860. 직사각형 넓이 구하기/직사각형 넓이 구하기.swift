import Foundation

func solution(_ dots:[[Int]]) -> Int {
    
    let sortedDots = dots.sorted { ($0[0], $0[1]) < ($1[0], $1[1]) }
    
    let a = sortedDots[0]
    let b = sortedDots[1]
    let c = sortedDots[2]
    
    let x = sqrt(pow(Double(a[0] - b[0]), 2) + pow(Double(a[1] - b[1]), 2))
    let y = sqrt(pow(Double(a[0] - c[0]), 2) + pow(Double(a[1] - c[1]), 2))
    
    return Int(x * y)
}