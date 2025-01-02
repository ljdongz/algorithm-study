import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t): # 10
    n = int(input())

    numbers = []
    dic = {}
    for _ in range(n): # 10 ^ 4
        numbers.append(input().rstrip())

    numbers.sort() 
    
    for number in numbers: # 10 ^ 4

        result = ""
        for num in number: # 10
            result += num

            if result in dic:
                result = ""
                break

        if result == "":
            print("NO")
            break
        else:
            dic[result] = True

    if len(dic) == len(numbers):
        print("YES")
        