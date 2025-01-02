import sys

input = sys.stdin.readline

A, B = list(map(int, input().split()))

result = -1

def backtrack(cur_sum, count):
    global result

    if cur_sum > B:
        return False
    elif cur_sum == B:
        result = count
        return True
    else:
        if backtrack(cur_sum * 10 + 1, count + 1):
            return True
        else:
            return backtrack(cur_sum * 2, count + 1)

backtrack(A, 1)
print(result)