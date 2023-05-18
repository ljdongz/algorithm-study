func solution(_ a:Int, _ b:Int) -> String {
    var days: [Int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    var week: [String] = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    var sum = 0
    for i in 0..<(a-1) {
        sum += days[i]
    }
    sum += b
    
    
    return week[sum%7]
}