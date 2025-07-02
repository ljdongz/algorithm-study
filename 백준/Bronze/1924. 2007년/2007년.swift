import Foundation

let monthInDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
let weeks = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

var calendar: [String: String] = [:]

var index = 0

for month in 1...monthInDays.count {
  let days = monthInDays[month - 1]

  for day in 1...days {
    calendar["\(month) \(day)"] = weeks[index % 7]
    index += 1
  }
}

let input = readLine()!
print(calendar[input]!)