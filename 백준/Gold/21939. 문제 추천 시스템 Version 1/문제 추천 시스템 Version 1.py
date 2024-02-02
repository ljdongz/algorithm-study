from collections import defaultdict
import sys, heapq

input = sys.stdin.readline

N = int(input())

problems = {}
minPQ = []
maxPQ = []

for _ in range(N):
    num, level = list(map(int, input().split()))
    problems[num] = level
    heapq.heappush(minPQ, (level, num))
    heapq.heappush(maxPQ, (level * -1, num * -1))

M = int(input())

for _ in range(M):
    cmd = list(map(str, input().split()))

    if cmd[0] == "add":
        # 문제 번호에 새로운 난이도 설정
        problems[int(cmd[1])] = int(cmd[2])
        heapq.heappush(minPQ, (int(cmd[2]), int(cmd[1])))
        heapq.heappush(maxPQ, (int(cmd[2]) * -1, int(cmd[1]) * -1))
    elif problems and cmd[0] == "solved":
        # problems에서 해당 문제 번호 삭제
        del problems[int(cmd[1])]
    elif problems and cmd[0] == "recommend":
        if cmd[1] == "1":
            # maxPQ의 우선순위 높은 데이터의 문제 번호가 추천 문제 리스트에 없는 경우 or
            # maxPQ의 우선순위 높은 데이터의 난이도가 추천 문제 리스트의 난이도와 일치하지 않는 경우
            while (maxPQ[0][1] * -1) not in problems or (maxPQ[0][0] * -1) != problems[maxPQ[0][1] * -1]:
                heapq.heappop(maxPQ)
            print(maxPQ[0][1] * -1)
        else:
            # minPQ의 우선순위 높은 데이터의 문제 번호가 추천 문제 리스트에 없는 경우 or
            # minPQ의 우선순위 높은 데이터의 난이도가 추천 문제 리스트의 난이도와 일치하지 않는 경우
            while minPQ[0][1] not in problems or minPQ[0][0] != problems[minPQ[0][1]]:
                heapq.heappop(minPQ)
            print(minPQ[0][1])