from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # 특정 과목의 선 이수 과목
        preCourse = defaultdict(list)
        # 특정 과목의 다음 이수 가능한 과목 
        nextCourse = defaultdict(list)

        # 맨 처음 이수할 수 있는 과목 리스트
        startList = [True] * numCourses
        
        visited = [False] * numCourses
        
        for start, end in prerequisites:

            # 맨 처음 이수 가능한 과목에서 제외
            startList[end] = False

            # 현재, 다음 과목이 같은 경우 or 서로가 선 이수 과목 조건인 경우
            if start == end or end in preCourse[start]:
                return False

            # 다음 이수 가능 과목 리스트 추가
            nextCourse[start].append(end)
            # 선 이수 과목 리스트 추가
            preCourse[end].append(start)
        
        for start, isStart in enumerate(startList):
            # 맨 처음 이수 가능한 과목인 경우
            if isStart:
                q = deque()
                q.append(start)
                visited[start] = True

                while q:
                    cur = q.popleft()

                    for next in nextCourse[cur]:
                        # 다음 이수 과목의 선 이수 과목 리스트에서 현재 과목 제거
                        preCourse[next].remove(cur)

                        # 남은 선 이수 과목이 존재하지 않은 경우 and 다음 이수 과목을 아직 이수하지 않은 경우
                        if len(preCourse[next]) == 0 and not visited[next]:
                            visited[next] = True
                            q.append(next)

        # 모든 과목을 이수하지 않은 경우
        if False in visited:
            return False
        else: 
            return True
