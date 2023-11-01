def solution(brown, yellow):
  sum = brown + yellow
  start = 1
  end = brown + yellow
  result = []

  while (start <= end):
    if start * end < sum:
      start += 1
    elif start * end > sum:
      end -= 1
    else:
      if (start - 2) * (end - 2) == yellow:
        result = [end, start]
      start += 1
      end -= 1

  return result