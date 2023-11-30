def solution(n):
    if n == 1 or n == 2:
        return n % 1234567
    
    a, b = 1, 2

    for i in range(n-2):
        b = a + b
        a = b - a
    
    return b % 1234567