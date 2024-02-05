def solution(m, n, board):

    answer = 0

    flag = True

    while flag:
        flag = False

        print(board)

        removeList = [[False] * n for _ in range(m)]

        for row in range(m-1):
            for col in range(n-1):
                if board[row][col] != "-" and board[row][col] == board[row+1][col] == board[row][col+1] == board[row+1][col+1]:
                    removeList[row][col] = True
                    removeList[row+1][col] = True
                    removeList[row][col+1] = True
                    removeList[row+1][col+1] = True
                    flag = True

        for lst in removeList:
            answer += lst.count(True)

        for row in range(m):
            for col in range(n):
                if removeList[row][col]:
                    board[row] = board[row][:col] + "-" + board[row][col+1:]

        for row in range(m-1, 1, -1):
            for col in range(n):
                if board[row][col] != "-":
                    continue

                for r in range(row, -1, -1):
                    if board[r][col] != "-":
                        board[row] = board[row][:col] + board[r][col] + board[row][col+1:]
                        board[r] = board[r][:col] + "-" + board[r][col+1:]
                        break
    
        
    return answer