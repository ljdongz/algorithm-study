import Foundation

func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {
    var result = 0
    var current = n
    while (!(current < a)) {
        let moc = current / a
        current -= (moc * a)
        current += moc * b
        result += moc * b
    }
    return result
}