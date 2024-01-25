def solution(m, n, puddles):
    
    dp = [[1] * m for _ in range(n)]

    for pCol, pRow in puddles:
        dp[pRow-1][pCol-1] = 0

    for row in range(0, n):
        for col in range(0, m):
            if row == 0 and row == col:
                continue

            if dp[row][col] == 0:
                continue

            if row == 0:
                dp[0][col] = dp[0][col-1]
            elif col == 0:
                dp[row][0] = dp[row-1][col]
            else:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

    return dp[-1][-1] % 1000000007