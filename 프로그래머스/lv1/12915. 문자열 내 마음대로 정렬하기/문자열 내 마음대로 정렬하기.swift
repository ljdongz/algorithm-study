func solution(_ strings:[String], _ n:Int) -> [String] {
    return strings.sorted {
        let left = $0[$0.index($0.startIndex, offsetBy: n)]
        let right = $1[$1.index($1.startIndex, offsetBy: n)]
        return left == right ? $0 < $1 : left < right
    }
}