import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M = int(input())

    arr = []
    for _ in range(M // 10 + 1):
        arr += list(map(int, input().split()))

    sortedArr = []
    resultArr = []

    for i, a in enumerate(arr):
        sortedArr.append(a)
        if i % 2 == 0:
            sortedArr.sort()
            resultArr.append(sortedArr[i//2])
    
    print(M // 2 + 1)

    cnt = 0
    for a in resultArr:
        if cnt == 10:
            cnt = 0
            print("")
        print(a, end=" ")
        cnt += 1