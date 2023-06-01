import Foundation

func solution(_ new_id:String) -> String {
    var check = "qwertyuiopasdfghjklzxcvbnm1234567890-_."
    var id = new_id.lowercased()
    
    id = String(id.filter({ check.contains($0) }))
    while(id.contains("..")) {
        id = id.replacingOccurrences(of: "..", with: ".")
    }
    if id.count > 0 && id.first! == "." { id.removeFirst() }
    if id.count > 0 && id.last! == "." { id.removeLast() }
    if id == "" { id = "a" }
    if id.count > 15 { id = String(id.prefix(15)) }
    if id.last! == "." { id.removeLast() }
    
    while(id.count < 3) {
        id += String(id.last!)
    }
    
    return id
}