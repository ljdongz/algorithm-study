def solution(arr1: list, arr2: list):
    answer = []

    newArr2 = []

    for col in range(len(arr2[0])):
        array = []
        for row in range(len(arr2)):
            array.append(arr2[row][col])
        newArr2.append(array)

    print(newArr2)

    for row in range(len(arr1)):
        array = []
        for i in range(len(newArr2)):
            sum = 0
            for col in range(len(arr1[0])):
                sum += arr1[row][col] * newArr2[i][col]
            array.append(sum)
        answer.append(array)

    return answer