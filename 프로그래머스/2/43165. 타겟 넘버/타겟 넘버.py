def solution(numbers: list, target):
    index = 0
    
    def dfs(index, current):
        if index == len(numbers):
            if current == 0:
                return 1
            else:
                return 0
        
        num = numbers[index]
        index += 1
        
        return dfs(index, (current-num)) + dfs(index, (current+num))
        
    
    return dfs(index, target)