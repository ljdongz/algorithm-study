from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # { 과목 : [[선 이수 과목], [다음 이수 가능 과목]]}
        preCourse = defaultdict(list)
        nextCourse = defaultdict(list)

        startList = [True] * numCourses
        visited = [False] * numCourses
        
        for start, end in prerequisites:
            
            startList[end] = False
            if start == end or end in preCourse[start]:
                return False
            
            nextCourse[start].append(end)
            preCourse[end].append(start)
        
        for start, isStart in enumerate(startList):
            if isStart:
                q = deque()
                q.append(start)
                visited[start] = True

                while q:
                    cur = q.popleft()

                    for next in nextCourse[cur]:

                        preCourse[next].remove(cur)
                        if len(preCourse[next]) == 0 and not visited[next]:
                            visited[next] = True
                            q.append(next)

                
        if False in visited:
            return False
        else: 
            return True