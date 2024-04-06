import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

# 회의 리스트
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

# 회의실 (회의 종료 시간을 담음)
rooms = [[0] for _ in range(K)]

result = 0

for meeting in meetings:
    rooms.sort(key=lambda x: x[-1], reverse=True)
    for room in rooms:
        if room[-1] < meeting[0]:
            room.append(meeting[1])
            result += 1
            break

print(result)

