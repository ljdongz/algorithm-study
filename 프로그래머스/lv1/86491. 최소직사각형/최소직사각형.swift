import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var a = sizes.map({$0.sorted()})
    
    var lmax = 0
    var rmax = 0
    
    for idx in 0..<a.count {
        if lmax < a[idx][0] { lmax = a[idx][0] }
        if rmax < a[idx][1] { rmax = a[idx][1] }
    }
    
    return lmax * rmax
}