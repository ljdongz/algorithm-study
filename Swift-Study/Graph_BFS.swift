//
//  Graph_BFS.swift
//  Swift-Study
//
//  Created by 이정동 on 1/6/25.
//

import Foundation

// 인접행렬 BFS
func bfsAdjMatrix(_ node: Int, _ edges: [[Int]]) {
  // V^2 크기의 공간 할당
  var adjMatrix: [[Int]] = .init(
    repeating: .init(
        repeating: 0,
        count: node + 1
    ),
    count: node + 1
  )
    
  for edge in edges {
    adjMatrix[edge[0]][edge[1]] = 1
    adjMatrix[edge[1]][edge[0]] = 1
  }

  var vis: [Bool] = .init(repeating: false, count: node + 1)
  var queue: [Int] = []
  var front = 0

  queue.append(1)
  vis[1] = true

  // 큐가 비어있을 때까지 반복
  while queue.count >= front + 1 {
    let cur = queue[front]
    front += 1
    print(cur)

		// 큐에서 뽑아준 노드와 연결도니 노드들을 보면서
    for degree in 1...node {
      // 연결되지 않은 노드 skip
      if adjMatrix[cur][degree] == 0 { continue }
      // 이미 방문한 노드라면 skip
      if vis[degree] { continue }

      queue.append(degree)
      vis[degree] = true
    }
  }
}


// 인접 리스트 BFS
// 시간 복잡도 -> V + 2E -> O(V+E)
// V + 2E인 이유 : 이미 방문한 노드를 또 한번 탐색하게 됨. but, 시간복잡도에서 계수는 제외.
func bfsAdjList(_ node: Int, _ edges: [[Int]]) {
  // 노드의 개수만큼 행을 구성 (각 행에 대한 열은 빈 배열로)
  var adjList: [[Int]] = .init(repeating: [], count: node + 1)
  // 연결된 노드끼리만 append
  for edge in edges {
    adjList[edge[0]].append(edge[1])
    adjList[edge[1]].append(edge[0])
  }

  var vis: [Bool] = .init(repeating: false, count: node + 1)
  var queue: [Int] = []
  var front = 0

  queue.append(1)
  vis[1] = true

  // 큐에 데이터가 존재할 때까지
  while queue.count >= front + 1 {
    let cur = queue[front]
    front += 1

    print(cur)
    
    // 특정 노드(p1)에 연결된 노드들만 순차 탐색 - O(D(p1))
    for degree in adjList[cur] {
      if vis[degree] { continue }
      queue.append(degree)
      vis[degree] = true
    }
  }
}



