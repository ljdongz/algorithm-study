def solution(A: list,B: list):
    answer = 0

    A.sort()
    B.sort()

    for i in range(len(A)):
      x = A[i]
      y = B[-(i+1)]

      answer += (x * y)
    return answer