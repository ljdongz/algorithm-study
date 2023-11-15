def solution(k, dungeons):
    answer = [0]

    def recursive(k, dungeons, index, count):
        if k < dungeons[index][0]:
            return

        copyDungeons = dungeons.copy()
        
        k -= copyDungeons[index][1]

        answer[0] = max(answer[0], count)

        copyDungeons.remove(copyDungeons[index])

        for i in range(len(copyDungeons)):
            recursive(k, copyDungeons, i, count + 1)

    for i in range(len(dungeons)):
        recursive(k, dungeons, i, 1)

    return answer[0]