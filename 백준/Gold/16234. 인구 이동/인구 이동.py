from collections import deque
import sys

N, L, R = list(map(int, sys.stdin.readline().split()))


flag = True
visited = []
drdc = [(0,1),(0,-1),(1,0),(-1,0)]
count = 0

countries = []
for _ in range(N):
    col = list(map(int, sys.stdin.readline().split()))
    countries.append(col)

def bfs(row, col):
    visited[row][col] = True
    q = deque()
    q.append((row, col))
    population = [countries[row][col]]
    coordinate = [(row, col)]
    global flag

    while q:
        cur_row, cur_col = q.popleft()
        for r, c in drdc:
            next_row = cur_row + r
            next_col = cur_col + c
            if next_row >= 0 and next_row < N and next_col >= 0 and next_col < N:
                gap = abs(countries[cur_row][cur_col] - countries[next_row][next_col])
                if gap >= L and gap <= R and not visited[next_row][next_col]:
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True
                    population.append(countries[next_row][next_col])
                    coordinate.append((next_row, next_col))
                    flag = True
    
    if flag:
        newPopulation = sum(population) // len(population)
        for r, c in coordinate:
            countries[r][c] = newPopulation

while flag:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                bfs(row, col)
    if flag:
        count += 1

print(count)