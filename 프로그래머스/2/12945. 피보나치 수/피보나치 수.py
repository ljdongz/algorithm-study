
def solution(n: int):

  a = 0
  b = 1
  result = 0

  for i in range(2, n+1):
    result = a + b
    if i % 2 == 0:
      a = result
    else:
      b = result

  return result % 1234567