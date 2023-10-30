def solution(n: int):
  
  initBin = bin(n)[2:]
  while True:
    n += 1

    nextBin = bin(n)[2:]

    if initBin.count("1") == nextBin.count("1"):
      return n
    
