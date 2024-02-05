import sys

input = sys.stdin.readline

N = int(input())

grape = [int(input()) for _ in range(N)]
dp = [0] * N

if N == 1:
    print(grape[0])
elif N == 2:
    print(grape[0] + grape[1])
else:
    dp[0] = grape[0]
    dp[1] = grape[0] + grape[1]
    dp[2] = max([grape[0] + grape[1], grape[0] + grape[2], grape[1] + grape[2]])

    for i in range(3, N):
        """
        1. i-2 까지 마실 수 있는 최대 총량 + i의 양 (연속 X)
        2. i-3 까지 마실 수 있는 최대 총량 + i-1의 양 + i의 양 (연속 O)
        3. i-1 까지 마실 수 있는 최대 총량 (현재량 포함 X)
            (i-1까지의 최대량은 i-2잔을 마시면서 연속 2잔을 마셨을 수 있기 때문에 i잔은 포함 X)
        """
        dp[i] = max([dp[i-2] + grape[i], dp[i-3] + grape[i-1] + grape[i], dp[i-1]])

    print(dp[-1])
