
import sys

input = sys.stdin.readline

N = int(input())

W = [list(map(int, input().split())) for _ in range(N)]

result = sys.maxsize

def backtrack(cur_idx, curr, sum):
    global result

    if len(curr) == N:
        if W[cur_idx][0] != 0:
            result = min(result, sum + W[cur_idx][0])
        return
    
    for i in range(N):
        if W[cur_idx][i] != 0 and i not in curr:
            curr.append(i)
            backtrack(i, curr, sum + W[cur_idx][i])
            curr.pop()


backtrack(0, [0], 0)

print(result)