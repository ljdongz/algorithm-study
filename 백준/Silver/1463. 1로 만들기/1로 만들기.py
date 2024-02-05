
N = int(input())

dp = [0, 0]

for i in range(2, N + 1):
    
    minList = [dp[i-1]]

    if i % 2 == 0:
        minList.append(dp[i//2])
    
    if i % 3 == 0:
        minList.append(dp[i//3])
    
    dp.append(min(minList) + 1)

print(dp[-1])