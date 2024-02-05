
import sys

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    string = input().rstrip("\n")

    left = 0
    right = len(string) - 1


    if string == string[::-1]:
        print(0)
        continue

    while left < right:

        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            if (string[left+1:right+1] == string[left+1:right+1][::-1]):
                print(1)
            elif string[left:right] == string[left:right][::-1]:
                print(1)
            else:
                print(2)
            break

            

    

