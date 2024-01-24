import math
 
N = int(input())

def fourSquare(n):
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            return 2
        
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
            
    return 4
    
print(fourSquare(N))