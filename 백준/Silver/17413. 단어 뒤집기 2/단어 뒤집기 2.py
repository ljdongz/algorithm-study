
import sys

input = sys.stdin.readline

S = input().rstrip("\n")

isTag = False
result = ""
reverseStr = ""

for c in S:

    if isTag:
        result += c
        if c == ">":
            isTag = False
    else:
        if c == "<":
            if reverseStr != "":
                result += reverseStr[::-1]
                reverseStr = ""
            result += c
            isTag = True
        elif c == " ":
            result += reverseStr[::-1] + c
            reverseStr = ""
        else:
            reverseStr += c

result += reverseStr[::-1]
    
print(result)