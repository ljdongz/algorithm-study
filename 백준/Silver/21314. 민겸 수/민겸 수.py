import sys

input = sys.stdin.readline

MKnum = input().rstrip()

def convert(mkStr):
    if len(mkStr) == 0:
        return ""

    if mkStr[-1] == "K":
        return str(5 * (10 ** (len(mkStr) - 1)))
    else:
        return str(10 ** (len(mkStr) - 1))

def maximum():
    cur_index = 0
    result = ""
    for i in range(len(MKnum)):
        if MKnum[i] == "K":
            result += convert(MKnum[cur_index:i+1])
            cur_index = i+1

    if cur_index != len(MKnum):
        result += "1" * (len(MKnum) - cur_index)

    print(result)

def minimum():
    cur_index = 0
    result = ""
    for i in range(len(MKnum)):
        if MKnum[i] == "K":
            result += convert(MKnum[cur_index:i]) + "5"
            cur_index = i+1
    
    if cur_index != len(MKnum):
        result += convert(MKnum[cur_index:])

    print(result)

maximum()
minimum()
