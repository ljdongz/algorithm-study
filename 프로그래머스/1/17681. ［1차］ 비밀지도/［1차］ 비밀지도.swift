func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    var answer: [String] = []
    
    for i in 0..<n {
        var num1 = arr1[i]
        var temp1 = ""
        for _ in 0..<n {
            temp1 = String(num1 % 2) + temp1
            num1 /= 2
        }
        
        var num2 = arr2[i]
        var temp2 = ""
        for _ in 0..<n {
            temp2 = String(num2 % 2) + temp2
            num2 /= 2
        }
        
        let s1 = temp1.map { String($0) }
        let s2 = temp2.map { String($0) }
        var result = ""
        for j in 0..<n {
            if s1[j] == "1" || s2[j] == "1" { result += "#" }
            else { result += " " }
        }
        answer.append(result)
    }
    
    return answer
}
