import Foundation

/*

남규 >= 영훈 + 2
택희 % 2 == 0

택희 2
*/

let N = Int(readLine()!)!

var result = 0
var taek_hee = 0

while taek_hee < N {
  taek_hee += 2

  if N - taek_hee - 2 < 0 { continue }

  let remain = N - taek_hee - 2
  // var nam_gyu = (remain / 2) + (remain % 2)
  var young_hoon = remain / 2

  while young_hoon > 0 {
    result += 1
    young_hoon -= 1
    // nam_gyu += 1
  }
}

print(result)