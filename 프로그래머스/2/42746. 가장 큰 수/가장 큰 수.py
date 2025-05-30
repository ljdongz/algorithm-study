def solution(numbers):
    nums = []
    result = ""
    
    for num in numbers:
        nums.append(((str(num) * 4), num))
    nums.sort(reverse = True)
    
    for num in nums:
        result += str(num[1])
        
    return str(int(result))