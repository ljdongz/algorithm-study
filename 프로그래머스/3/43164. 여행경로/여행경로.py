

def solution(tickets: list):
    answer = []
    route = []

    pathGraph = {}
    count = {}

    for start, end in tickets:
        if start in pathGraph:
            pathGraph[start].append(end)
        else:
            pathGraph[start] = [end]

        if start+end in count:
            count[start+end] += 1
        else:
            count[start+end] = 1

    def dfs(start, current, visited, count):
        visited.append([start, current])
        count[start+current] -= 1

        if len(visited) == len(tickets):
            route.append(visited)
            return
        
        if current not in pathGraph:
            return

        for end in pathGraph[current]:
            if [current, end] not in visited or count[current+end] != 0:
                dfs(current, end, visited.copy(), count.copy())


    for end in pathGraph["ICN"]:
        dfs("ICN", end, [], count.copy())

    route.sort()
    route = route[0]

    for start, end in route:
        answer.append(start)
    answer.append(route[-1][1])

    return answer