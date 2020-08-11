import heapq


def solution(jobs):
    jobs.sort()
    wait = []
    start, time = jobs.pop(0)
    end = start + time

    answer = 0
    answer += time
    jobs_len = len(jobs)
    cnt = 0
    idx = 0

    while cnt < jobs_len:
        for i in range(idx, jobs_len):
            start, time = jobs[i]
            if start <= end:
                heapq.heappush(wait, jobs[i][1])
                answer -= jobs[i][0]
                idx = i + 1
            else:
                idx = i
                break

        if len(wait) > 0:
            wait_first = heapq.heappop(wait)
            answer += end + wait_first
            end += wait_first
            cnt += 1
        else:
            start, time = jobs[idx]
            end = start + time
            answer += time
            idx += 1
            cnt += 1

    return answer // (jobs_len + 1)
