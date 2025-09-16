import Foundation

func solution(_ data:[[Int]], _ col:Int, _ row_begin:Int, _ row_end:Int) -> Int {
    
    let sortedData = data.sorted { 
        let first = ($0[col-1], -$0[0])
        let second = ($1[col-1], -$1[0])
        return first < second
    }
    
    var bits: [[Int]] = []
    
    for row in row_begin...row_end {
        var mod = 0
        for col in sortedData[row - 1] {
            mod += col % row
        }
        
        var bit: [Int] = []
        for i in 0..<20 {
            bit.append(mod % 2)
            mod /= 2
        }
        bits.append(bit.reversed())
    }
    
    if bits.isEmpty { return 0 }
    
    var resultBit: [Int] = .init(repeating: 0, count: 20)
    for bit in bits {
        var temp: [Int] = []
        
        for i in 0..<20 {
            temp.append(resultBit[i] == bit[i] ? 0 : 1)
        }
        
        resultBit = temp
    }
    
    var result = 0

    for i in 0..<20 {
        result += Int(pow(Double(2), Double(i))) * resultBit[20 - i - 1]
    }
    
    return result
}