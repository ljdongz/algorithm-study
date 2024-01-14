def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]

    stack = []

    for index, num in enumerate(numbers):

        # stack이 비어있지 않고, stack의 마지막 숫자가 현재 비교할 숫자보다 작을 때까지
        while stack and stack[-1][1] < num:
            idx, _ = stack.pop()
            answer[idx] = num

        stack.append((index, num))

    return answer