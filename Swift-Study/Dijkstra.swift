
struct Edge: Comparable {
  let destinaion: Int
  let cost: Int
  
  static func < (lhs: Edge, rhs: Edge) -> Bool {
    lhs.cost < rhs.cost
  }
}

/**
 - Complexity: O(E * logE)
    - 간선 개수(E) * 힙 삭제 비용(logE)
 */
func dijkstra(_ node: Int, _ edges: [[Int]], _ start: Int) {
    var adjList: [[Edge]] = .init(repeating: [], count: node + 1)
    for edge in edges {
        adjList[edge[0]].append(Edge(destinaion: edge[1], cost: edge[2]))
    }
    
    var heap = Heap<Edge>()
    var distance: [Int] = .init(repeating: .max / 2, count: node + 1)
    heap.insert(with: Edge(destinaion: start, cost: 0))
    distance[start] = 0
    
    while !heap.isEmpty {
        let cur = heap.delete()!
        
        // Heap에 나를 넣어준 노드보다 이후에 결정된 노드를 통해 가는 경로가 더 최단 경로가 되는 경우
        if distance[cur.destinaion] != cur.cost { continue }
        
        for degree in adjList[cur.destinaion] {
            // 이전에 결정된 노드를 통해 결정된 최소값이 더 작은 경우 skip
            if distance[degree.destinaion] <= distance[cur.destinaion] + degree.cost { continue }
            
            // 새롭게 추가된 노드를 통해 해당 노드로 가는 경로가 더 cost가 작은 경우 update
            distance[degree.destinaion] = distance[cur.destinaion] + degree.cost
            heap.insert(with: Edge(destinaion: degree.destinaion, cost: distance[degree.destinaion]))
        }
    }
    
    for i in 1...node {
        print(distance[i], terminator: " ")
    }
    print("")
}
