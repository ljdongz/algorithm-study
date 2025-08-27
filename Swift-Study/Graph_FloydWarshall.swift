/**
 Find `Rechability` in Directed Graph
 */
func floyd(_ node: Int, _ edges: [[Int]]) {
    var t: [[Bool]] = .init(
        repeating: .init(
            repeating: false,
            count: node + 1
        ),
        count: node + 1
    )
    
    // edge[0] -> edge[1] 연결을 표시
    for edge in edges {
        t[edge[0]][edge[1]] = true
    }
    
    // [j][i] && [i][k] == [j][k]
    // O(V^3)
    // 1_000_ 000_000
    for i in 1...node {
        for j in 1...node {
            for k in 1...node {
                if t[j][i] && t[i][k] { t[j][k] = true }
            }
        }
    }
    
    for y in 1...node {
        for x in 1...node {
            t[y][x] ? print("1", terminator: " ") : print("0", terminator: " ")
        }
        print("")
    }
}