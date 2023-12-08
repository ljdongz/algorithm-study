def solution(nums: list):
    answer = 0
    count = len(nums) / 2
    dict = {}

    for num in nums:
        if num in dict:
            dict[num] +=1
        else:
            dict[num] = 1

    for _ in dict:
        if count == 0:
            break

        count -= 1
        answer += 1

    return answer