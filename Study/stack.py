string = {"(": ")", "{": "}", "[": "]"}


def validParentheses(value) -> bool:
  inStack = list(value)
  outStack = []
  while(len(inStack) > 0):
    
    out = inStack.pop()

    if out not in string:
      outStack.append(out)
      continue
    
    if len(outStack) == 0:
      return False
    
    result = outStack.pop()

    if string[out] != result:
      return False
  
  if len(outStack):
    return False
  else:
    return True
  
  
def isValid(s):
  stack = []
  for p in s:
    if p == "(":
      stack.append(")")
    elif p == "{":
      stack.append("}")
    elif p == "[":
      stack.append("]")
    else:
      if not stack or stack.pop() != p:
        return False
  
  return not stack

print(isValid("()"))

lst = [""]
print(not lst)
