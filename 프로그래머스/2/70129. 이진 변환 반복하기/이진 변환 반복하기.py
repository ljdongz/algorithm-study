def solution(s: str):
  
  zeroCount = 0
  changeCount = 0

  while s != "1":
    zeroCount += s.count("0")

    s = bin(s.count("1"))[2:]

    changeCount += 1
  
  return [changeCount, zeroCount]