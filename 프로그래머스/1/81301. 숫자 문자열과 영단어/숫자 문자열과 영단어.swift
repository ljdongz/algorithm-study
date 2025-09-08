import Foundation

func solution(_ s:String) -> Int {
    let num: Set<String> = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    let words: [String: String] = [
        "zero": "0", "one" : "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    ]
    var result = ""
    var temp = ""
    let newS = s.map { String($0) }
    
    for s in newS {
        if num.contains(s) { 
            result += s 
            continue
        }
        
        temp += s
        
        if let word = words[temp] {
            result += word
            temp = ""
        }
    }
    
    return Int(result)!
}