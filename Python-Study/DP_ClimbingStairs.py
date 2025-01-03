
# BottomUP
def climbing_stairs_bottomup(n):
    if n == 1 or n == 2:
        return n
    
    a = 1
    b = 2

    for i in range(n-2):
        temp = b
        b = a + b
        a = temp

    return b


# TopDown
result = {}

def climbing_stairs_topdown(n):
    if n == 1 or n == 2:
        result[n] = n

    if n not in result:
        result[n] = climbing_stairs_topdown(n-1) + climbing_stairs_topdown(n-2)

    return result[n]

