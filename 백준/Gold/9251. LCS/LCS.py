import sys

input = sys.stdin.readline

s1 = " " + input().rstrip()
s2 = " " + input().rstrip()

memo = [[0] * len(s2) for _ in range(len(s1))]

maxLength = 0

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])

        maxLength = max(maxLength, memo[i][j])


print(maxLength)