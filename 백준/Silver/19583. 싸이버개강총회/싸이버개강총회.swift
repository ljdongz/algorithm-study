import Foundation

// 1) 시작 전 대화 여부
// 2) 총회 종료 - 스트리밍 종료 사이의 대화 여부

let input = readLine()!.split(separator: " ")
let S = input[0].split(separator: ":").map { Int(String($0))! } // 총회 시작
let E = input[1].split(separator: ":").map { Int(String($0))! } // 총회 종료
let Q = input[2].split(separator: ":").map { Int(String($0))! } // 스트리밍 종료

let sTime = S[0] * 100 + S[1]
let eTime = E[0] * 100 + E[1]
let qTime = Q[0] * 100 + Q[1]

var log = Set<String>()
var check = Set<String>()
var count = 0

while let line = readLine() {
  let chatLog = line.split(separator: " ")
  let time = chatLog[0].split(separator: ":").map { Int(String($0))! }
  let user = String(chatLog[1])

  if (time[0] * 100 + time[1]) <= sTime {
    log.insert(user)
    continue
  }

  if eTime <= (time[0] * 100 + time[1]) && (time[0] * 100 + time[1]) <= qTime {
    if log.contains(user) && !check.contains(user) {
       count += 1 
       check.insert(user)
    }
  }
}

print(count)