import Foundation

func solution(_ data:[[Int]], _ col:Int, _ row_begin:Int, _ row_end:Int) -> Int {
    
    let sortedData = data.sorted { 
        let first = ($0[col-1], -$0[0])
        let second = ($1[col-1], -$1[0])
        return first < second
    }
    
    var bits: [Int] = []
    
    for row in row_begin...row_end {
        var bit = 0
        for col in sortedData[row - 1] {
            bit += col % row
        }
        
        bits.append(bit)
    }
    
    var result = 0
    
    for bit in bits {
        result ^= bit
    }
    
    return result
}