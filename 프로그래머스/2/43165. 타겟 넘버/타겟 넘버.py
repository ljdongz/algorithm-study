

def solution(numbers: list, target):
    answer = 0

    def dfs(current, op, index):
        
        if op == "+":
            current += numbers[index]
        elif op =="-":
            current -= numbers[index]

        if index == len(numbers) - 1:
            if current == target:
                return 1
            else:
                return 0

        left = dfs(current, "-", index + 1)
        right = dfs(current, "+", index + 1)

        return left + right

    left = dfs(0, "-", 0)
    right = dfs(0, "+", 0)


    return left + right