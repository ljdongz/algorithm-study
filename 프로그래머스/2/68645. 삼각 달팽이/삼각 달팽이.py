
def solution(n):
    answer = []
    triangle = [[0] * (i + 1) for i in range(n)]
    row, col = -1, 0
    num = 1

    while n > 0:
        for _ in range(n):
            row += 1
            triangle[row][col] = num
            num += 1
            

        n -= 1
        if n == 0: break

        for _ in range(n):
            col += 1
            triangle[row][col] = num
            num += 1
            
        n -= 1
        if n == 0: break

        for _ in range(n):
            row -= 1
            col -= 1
            triangle[row][col] = num
            num += 1

        n -= 1

    for trg in triangle:
        answer += trg

    return answer