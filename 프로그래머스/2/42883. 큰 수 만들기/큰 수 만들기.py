def solution(number, k):

    number = list(map(int, number))
    stack = []

    for num in number:
        if k == 0:
            stack.append(num)
            continue

        if not stack or stack[-1] >= num:
            stack.append(num)
        else:
            while stack and stack[-1] < num and k > 0:
                stack.pop()
                k -= 1
            stack.append(num)
    
    while k > 0:
        stack.remove(min(stack))
        k -= 1

    return "".join(list(map(str, stack)))