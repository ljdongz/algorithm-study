func solution(_ a:Int, _ b:Int) -> String {
    let days: [Int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let week: [String] = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    let totalDay = days[0..<a-1].reduce(0, +) + b
    
    
    return week[totalDay%7]
}