import Foundation

func solution(_ keymap:[String], _ targets:[String]) -> [Int] {
    var result: [Int] = []

    for target in targets {
        var count = 0
        for t in target {
            var keyCount: [Int] = []
            for key in keymap {
                keyCount.append(Array(key).firstIndex(of: t) ?? -1)
            }
            keyCount.removeAll { $0 == -1 }
            if keyCount.isEmpty {
                count = -1
                break
            } else {
                count += keyCount.min()! + 1
            }
        }
        result.append(count)
    }
    return result
}