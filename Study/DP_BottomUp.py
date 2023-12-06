
result = {
    1: 1,
    2: 1
}

def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    for i in range(3, n+1):
        result[i] = result[i-1] + result[i-2]

    return result[n]