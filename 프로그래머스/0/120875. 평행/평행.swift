import Foundation

func solution(_ dots:[[Int]]) -> Int {
    
    var dots = dots.sorted { ($0[0], $0[1]) < ($1[0], $1[1]) }
    
    let x = dots[0]
    let y = dots[1]
    let z = dots[2]
    let w = dots[3]
    
    let a = Double(y[1] - x[1]) / Double(y[0] - x[0]) == Double(w[1] - z[1]) / Double(w[0] - z[0])
    let b = Double(z[1] - x[1]) / Double(z[0] - x[0]) == Double(w[1] - y[1]) / Double(w[0] - y[0])
    let c = Double(w[1] - x[1]) / Double(w[0] - x[0]) == Double(z[1] - y[1]) / Double(z[0] - y[0])
    
    return a || b || c ? 1 : 0
}