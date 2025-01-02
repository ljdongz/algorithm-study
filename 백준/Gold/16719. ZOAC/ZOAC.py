
import sys

input = sys.stdin.readline

string = list(input().rstrip())

stringArray = []
for idx, s in enumerate(string):
    stringArray.append((s, idx))

visited = [False] * len(string)
stack = [0]

while stack:
    alphabet = ("Z", 99)

    if False not in visited[stack[-1]:]:
        stack.pop()
        continue

    for string in stringArray[stack[-1]:]:
        if visited[string[1]]:
            break
        alphabet = min(alphabet, string)
    
    visited[alphabet[1]] = True
    stack.append(alphabet[1]+1)

    result = ""
    for idx, bool in enumerate(visited):
        if bool:
            result += stringArray[idx][0]
    print(result)