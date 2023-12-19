# Bottom Up

def solution(triangle: list):

    for i in range(len(triangle)-1, 0, -1):
        for j in range(len(triangle[i-1])):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])

    return triangle[0][0]


# Top Down
# 시간 초과
def solution(triangle: list):

    def dp(row, col):
        if row == len(triangle) - 1:
            return triangle[row][col]

        return triangle[row][col] + max(dp(row+1, col), dp(row+1, col+1))

    return dp(0, 0)
