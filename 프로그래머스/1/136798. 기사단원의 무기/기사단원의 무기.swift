import Foundation

func solution(_ number:Int, _ limit:Int, _ power:Int) -> Int {
    var total = 0
    
    for i in 1...number {
        var count = 0
        
        for j in 1...Int(sqrt(Double(i))) {
            if i % j == 0 {
                count += 1
                if j != i / j {
                    count += 1
                }
            }
        }
        
        total += (count > limit) ? power : count
    }
    
    return total
}