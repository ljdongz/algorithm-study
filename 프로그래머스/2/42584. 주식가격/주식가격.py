
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):

        for time, price in stack:
            answer[time] += 1

        while stack and stack[-1][1] > prices[i]:
            stack.pop()
        stack.append((i, prices[i]))

    return answer