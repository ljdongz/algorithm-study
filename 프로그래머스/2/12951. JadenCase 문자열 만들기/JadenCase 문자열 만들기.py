
def solution(s: str):
  answer = ''
  strings = s.split(" ")

  for i in range(len(strings)):

    if strings[i] == " ": 
      answer += ""
      continue

    answer += strings[i].capitalize()
    if i == len(strings) - 1: break
    answer += " "

  return answer