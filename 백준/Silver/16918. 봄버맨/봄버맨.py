import sys

input = sys.stdin.readline

R, C, N = list(map(int, input().split()))

bomb = [[-1] * C for _ in range(R)]

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
value = {
  -1 : ".",
  0 : "O",
  1 : "O",
  2 : "O"
}

for row in range(R):
  state = input().rstrip()
  col = 0
  for s in state:
    if s == "O":
      bomb[row][col] = 0
    col += 1

time = 0
for _ in range(N):
  time += 1

  for row in range(R):
    for col in range(C):
      if bomb[row][col] != -1 or time % 2 == 0:
        bomb[row][col] += 1
        # 터지는 폭탄
        if bomb[row][col] == 3:
          bomb[row][col] = -1

          for r, c in dir:
            next_row = row + r
            next_col = col + c

            if next_row >= 0 and next_row < R and next_col >= 0 and next_col < C:
              if (r == 1 or c == 1) and bomb[next_row][next_col] == 2:
                continue
              bomb[next_row][next_col] = -1

for r in range(R):
  for c in range(C):
    print(value[bomb[r][c]], end="")
  print("")

