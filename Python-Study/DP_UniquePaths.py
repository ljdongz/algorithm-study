

def uniquePaths_topDown(m, n):
    # 딕셔너리를 사용한 방법
    memo = {}

    def grid(m, n):
        if m == 0 or n == 0:
            return 1
        
        if (m, n) not in memo:
            memo[(m, n)] = grid(m-1, n) + grid(m, n-1)
        
        return memo[(m, n)]
    
    return grid(m-1, n-1)

print(uniquePaths_topDown(3,7))

def uniquePaths_bottomUp(m, n):
    # 배열을 사용한 방법
    memo = [[0]*n for _ in range(m)]

    for i in range(m):
        memo[i][0] = 1
    for j in range(n):
        memo[0][j] = 1

    for row in range(1, m):
        for col in range(1, n):
            memo[row][col] = memo[row-1][col] + memo[row][col-1]

    return memo[m-1][n-1]

print(uniquePaths_bottomUp(3, 2))