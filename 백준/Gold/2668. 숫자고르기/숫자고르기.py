import sys

input = sys.stdin.readline

N = int(input())

nums = [[0] * (N+1) for _ in range(2)]

for i in range(1, N+1):
    nums[0][i] = i
    nums[1][i] = int(input())

result = []
visited = [False] * (N+1)

def dfs(init, cur):
    vst.append(cur)

    next = nums[1][cur]

    if visited[next]:
        return

    if next in vst:
        if init == next:
            for v in vst:
                visited[v] = True
                result.append(v)
    else:
        dfs(init, next)

for i in range(1, N+1):
    vst = []
    dfs(i, i)

result.sort()

print(len(result))
for r in result:
    print(r)