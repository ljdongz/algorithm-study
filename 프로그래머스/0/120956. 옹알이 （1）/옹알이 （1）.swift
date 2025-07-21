import Foundation

func solution(_ babbling:[String]) -> Int {
  let words = ["aya", "ye", "woo", "ma"]

  var combines: [String] = []
  var visited: [Bool] = [false, false, false, false]
  var result = 0

  // k: 현재 뽑은 개수
  // m: 뽑아야 하는 총 개수
  func recursive(k: Int, m: Int, word: String) {
    if k == m {
      combines.append(word)
      return
    }

    for i in 0..<4 {
      if !visited[i] {
        visited[i] = true
        recursive(k: k + 1, m: m, word: word + words[i])
        visited[i] = false
      }
    }
  }

  for i in 1...4 {
    recursive(k: 0, m: i, word: "")
  }

  for bab in babbling {
    if combines.contains(bab) {
      result += 1
    }
  }

  return result
}