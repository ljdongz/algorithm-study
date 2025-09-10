import Foundation

/* 
scehdules : 출근 희망 시각
timelogs : 출근한 시각
startday : 이벤트 시작 요일
*/

// startday % 7 == (6 || 0) -> 주말

func solution(_ schedules:[Int], _ timelogs:[[Int]], _ startday:Int) -> Int {
    
    var results: [Int] = .init(repeating: 0, count: schedules.count)
    
    // 유저 순회
    for userID in 0..<schedules.count {
        // userID의 목표 시각
        var schedule = schedules[userID] + 10
        if (schedule % 100) / 60 >= 1 { 
            schedule += (100 - 60)
        }
        
        // 현재 날짜
        var day = startday
        
        // userID의 n일차 출근 시각
        for log in timelogs[userID] {
            // 평일인 경우
            if day % 7 < 6 && day % 7 > 0 { 
                // 정시 출근인 경우
                if schedule >= log {
                    results[userID] += 1
                }
            } else {
                results[userID] += 1
            }
            
            day += 1
        }
    }
    
    return results.filter { $0 == 7 }.count
}