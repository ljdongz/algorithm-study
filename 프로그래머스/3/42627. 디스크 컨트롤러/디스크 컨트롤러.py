import heapq

def solution(jobs: list):

    jobs.sort()
    pq = []
    cur_time = 0
    total_task = 0
    length = len(jobs)

    while jobs or pq:
        for _ in range(len(jobs)):
            job = jobs[0]
            if cur_time < job[0]:
                break
            heapq.heappush(pq, (job[1], job[0]))
            jobs.remove(job)
            
        if pq:
            task, req = heapq.heappop(pq)
            total_task += (task + cur_time - req)
            cur_time += task
        else:
            cur_time += 1


    return total_task // length