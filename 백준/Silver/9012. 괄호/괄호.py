N = int(input())

def isValid(ps):
    for s in ps:
        if s == '(':
            stack.append(')')
        elif not stack or stack.pop() != s:
            return "NO"

    if stack: return "NO"
    else: return "YES"


for i in range(N):
    ps = input()
    stack = []

    print(isValid(ps))