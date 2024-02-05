

"""
N번째 계단까지 오를 때 얻을 수 있는 최댓값의 경우의 수

Case 1. N-2칸에서 2칸 이동
    dp[N] = dp[N-2] + N번째 계단의 점수
Case 2. N-1칸에서 1칸 이동 (여기서는 N-3칸에서 N-1칸으로 이동한다는 조건이 필요)
    dp[N] = dp[N-3] + N-1번째 계단의 점수 + N번째 계단의 점수
"""

N = int(input())

stairs = [int(input()) for _ in range(N)]

dp = [0] * N

if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
elif N == 3:
    print(max(stairs[0], stairs[1]) + stairs[2])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0], stairs[1]) + stairs[2]

    for i in range(3, N):
        a = dp[i-3] + stairs[i-1]
        b = dp[i-2]

        dp[i] = max(a, b) + stairs[i]

    print(dp[-1])

