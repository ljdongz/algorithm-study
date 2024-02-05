N = int(input())

memo = {
    1: 1,
    2: 2,
    3: 4
}

def recursive(n):
    if n in memo:
        return memo[n]
    
    if n not in memo:
        memo[n] = recursive(n-1) + recursive(n-2) + recursive(n-3)

    return memo[n]

for _ in range(N):
    n = int(input())
    print(recursive(n))