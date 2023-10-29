def solution(s: str):
  strings = s.split(" ")
  result = []
  for c in strings:

    if c == "": 
      result.append("")
      continue

    result.append(c.capitalize())

  return " ".join(result)