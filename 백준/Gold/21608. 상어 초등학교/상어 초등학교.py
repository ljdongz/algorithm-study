
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

seat = [[0] * N for _ in range(N)] # 좌석 배치도

students = [] # 학생 순서
fav_students = defaultdict(list) # 학생별 좋아하는 학생 리스트
for _ in range(N**2):
    lst = list(map(int, input().split()))
    students.append(lst[0])
    fav_students[lst[0]] = (lst[1:])

seat[1][1] = students[0] # 첫번째 학생 좌석 설정

drdc = [(1,0), (-1,0), (0,1), (0,-1)]

result = 0

# 모든 학생 접근
for student in students[1:]:
    fav_stu = fav_students[student] # 좋아하는 학생 리스트

    # 인접한 좋아하는 학생 수, 인접한 비어있는 좌석 수, 행, 열
    # (우선순위 순으로 비교하기 위해 학생수, 비어있는 좌석 수를 음수 값으로 넣고 비교할 예정)
    # ex) best_seat = min(best_seat, (-학생수, -좌석 수, 행, 열))
    best_seat = (0, 0, N-1, N-1) 
    for row in range(N):
        for col in range(N):
            if seat[row][col] != 0: # 이미 있는 좌석이면 건너뛰기
                continue

            fav_count = 0
            empty_count = 0

            for r, c in drdc:
                next_row = row + r
                next_col = col + c
                if next_row >= 0 and next_row < N and next_col >= 0 and next_col < N:
                    if seat[next_row][next_col] == 0:
                        empty_count += 1
                    elif seat[next_row][next_col] in fav_stu:
                        fav_count += 1
            
            best_seat = min(best_seat, (-fav_count, -empty_count, row, col))

    seat[best_seat[2]][best_seat[3]] = student

for row in range(N):
    for col in range(N):
        student = seat[row][col]
        fav_stu = fav_students[student]

        fav_count = 0
        for r, c in drdc:
            next_row = row + r
            next_col = col + c
            if next_row >= 0 and next_row < N and next_col >= 0 and next_col < N:
                if seat[next_row][next_col] in fav_stu:
                    fav_count += 1

        result += int(10**(-1 + fav_count))

print(result)