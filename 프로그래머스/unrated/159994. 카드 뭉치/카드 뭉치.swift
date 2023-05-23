import Foundation

func solution(_ cards1:[String], _ cards2:[String], _ goal:[String]) -> String {
    var c1 = cards1
    var c2 = cards2
    var check = 0
    var currentCard = 0
    var goalIndex = 0
    while(check != 2 && goalIndex != goal.count) {
        var cards = currentCard % 2 == 0 ? c1 : c2
        if (cards.first ?? "" == goal[goalIndex]) {
            currentCard % 2 == 0 ? c1.removeFirst() : c2.removeFirst()
            check = 0
            goalIndex += 1
        } else {
            check += 1
            currentCard += 1
        }
    }
    
    return check == 2 ? "No" : "Yes"
}