
"""
<<< DP 접근 방법 (Top Down) >>>
1. 크고 작은 문제를 하위 문제로 나눔 
    - fib(7) = fib(5) + fib(6)
    - 따라서 fib(5), fib(6) 값을 구한다.
2. 하위 문제에 대한 답을 계산
    - 중복 하위 문제들에 대하여,
    - 계산 결과를 메모리에 저장하여 중복된 문제에 사용한다.
3. 하위 문제에 대한 답으로 원래 문제에 대한 답을 계산

-> 재귀 사용
"""

result = {}

def fib(n):
    if n == 1 or n == 2:
        return 1
    
    # n에 대한 값이 메모리에 저장되어 있지 않다면,
    if n not in result:
        # 계산 결과를 메모리에 저장
        result[n] = fib(n-1) + fib(n-2) 

    # n에 대한 값을 리턴
    return result[n]