
"""
후위 표기식
1. 피연산자 그대로 출력
2. 스택이 비어있는 경우에는 스택에 연산자 바로 추가
3. stack의 top이 자신보다 우선순위가 낮은 연산자를 만날 때까지 pop하고 자신을 추가
    (단, 여는 괄호를 만날 때 pop하지 않고 그대로 종료)
4. 닫는 괄호인 경우에는 여는 괄호가 나올 때까지 pop
5. 표기식 내 모든 문자를 순환 후 stack에 남아있는 모든 값들을 pop
"""

notation = input()

stack = []

priority = {"+": 0, "-": 0, "*": 1, "/": 1}

for c in notation:
    if c not in ["+", "-", "*", "/", "(", ")"]:
        print(c, end="")
    elif not stack or c == "(":
        stack.append(c)
    elif c == ")":
        while stack[-1] != "(":
            print(stack.pop(), end="")
        stack.pop()
    else:
        while stack and stack[-1] != "(" and priority[stack[-1]] >= priority[c]:
            print(stack.pop(), end="")
        stack.append(c)
    
while stack:
    print(stack.pop(), end="")