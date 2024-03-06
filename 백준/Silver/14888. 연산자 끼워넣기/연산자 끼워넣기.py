
import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

operate = list(map(int, input().split()))

op_count = {
    "+" : operate[0],
    "-" : operate[1],
    "*" : operate[2],
    "//" : operate[3]
}

op_list = []

minimum = sys.maxsize
maximum = -sys.maxsize - 1

def backtrack(curr):
    if len(curr) == N-1:
        op_list.append(curr[:])
        return
    
    for op in ["+", "-", "*", "//"]:
        if curr.count(op) < op_count[op]:
            curr.append(op)
            backtrack(curr)
            curr.pop()

backtrack([])

for operate in op_list:
    numss = nums[:]
    for idx, op in enumerate(operate):
        if op == "+":
            numss[idx+1] = numss[idx] + numss[idx+1]
        elif op == "-":
            numss[idx+1] = numss[idx] - numss[idx+1]
        elif op == "*":
            numss[idx+1] = numss[idx] * numss[idx+1]
        else:
            if numss[idx+1] == 0:
                break
            elif numss[idx] > 0:
                numss[idx+1] = numss[idx] // numss[idx+1]
            else:
                numss[idx+1] = (-numss[idx] // numss[idx+1]) * -1

    maximum = max(maximum, numss[-1])
    minimum = min(minimum, numss[-1])
    
print(maximum)
print(minimum)