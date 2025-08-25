import Foundation

let dldrdc = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

while true {
  let input = readLine()!.split(separator: " ").map { Int(String($0))! }
  let L = input[0]
  let R = input[1]
  let C = input[2]

  if L == 0 && R == 0 && C == 0 { break }

  var board: [[[String]]] = []
  var visited: [[[Int]]] = .init(
      repeating: .init(
        repeating: .init(
          repeating: 0,
          count: C
        ),
        count: R
      ),
      count: L
    )
  
  var success: (Int, Int, Int)?
  var queue: [(Int, Int, Int)] = []
  var front = 0

  for l in 0..<L {
    var arr: [[String]] = []
    for r in 0..<R {
      let input = readLine()!.map { String($0) }
      arr.append(input)

      if let c = arr[r].firstIndex(where: { $0 == "S" }) {
        queue.append((l, r, c))
        arr[r][c] = "#"
      }
    }
    board.append(arr)
    _ = readLine()!
  }

  while queue.count >= front + 1 {
    let (curL, curR, curC) = queue[front]
    front += 1
    
    if board[curL][curR][curC] == "E" { 
      success = (curL, curR, curC)
    }

    for (dl, dr, dc) in dldrdc {
      let nextL = curL + dl
      let nextR = curR + dr
      let nextC = curC + dc

      if nextL >= 0 && nextL < L && nextR >= 0 && nextR < R && nextC >= 0 && nextC < C {
        if board[nextL][nextR][nextC] != "#" && visited[nextL][nextR][nextC] == 0 {
          queue.append((nextL, nextR, nextC))
          visited[nextL][nextR][nextC] = visited[curL][curR][curC] + 1
        }
      }
    }
  }

  if let (l, r, c) = success {
    print("Escaped in \(visited[l][r][c]) minute(s).")
  } else {
    print("Trapped!")
  }
}



