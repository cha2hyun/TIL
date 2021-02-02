def solution(jobs):
    import heapq
    answer, cnt, last = 0, 0, -1
    heap = []
    jobs.sort()
    time = jobs[0][0]
    while cnt < len(jobs):
        for start, term in jobs:            
            if last < start <= time :
                heapq.heappush(heap, (term, start))                        
        if heap:            
            term, start = heapq.heappop(heap)            
            last = time
            time += term
            answer += (time - start)
            cnt += 1
        else:
            time += 1
        


# def solution(jobs):
#     import heapq
#     from collections import deque

#     N = len(jobs)
#     jobs = deque(sorted(jobs))
#     jobs_done = 0
#     cand = []
#     curr_time = 0
#     total_time = 0
    
#     print(jobs)
#     while jobs_done < N:
#         # 최초
#         if not cand:
#             start_time, need_time = jobs.popleft()
#             curr_time = start_time + need_time
#             total_time += curr_time
#         # 아니믄
#         else:
#             need_time, start_time = heapq.heappop(cand)
#             curr_time += need_time
#             total_time += curr_time - start_time
#         while jobs and jobs[0][0] <= curr_time:
#             heapq.heappush(cand, jobs.popleft()[::-1])
#         jobs_done += 1
#     return total_time // N




# import heapq
# from collections import deque
# def solution(jobs):
#     N, REQUEST = len(jobs), 0
#     jobs = deque(sorted(jobs))
#     jobs_done, curr_time, waits, cand = 0, 0, 0, []
#     # 일을 다 마칠 때 까지
#     while jobs_done < N:
#         # 요청이 들어온 것이 없을 때
#         if not cand:            
#             request, time = jobs.popleft()                        
#             curr_time = request + time
#             waits += time
#         # 요청이 들어온 것이 있을 때
#         else:
#             time, request = heapq.heappop(cand)
#             curr_time += time
#             waits += curr_time - request

#         jobs_done += 1
            
#         while jobs and jobs[0][REQUEST] <= curr_time:
#             heapq.heappush(cand, jobs.popleft()[::-1])
            
#     return waits // N


# def solution(jobs):
#     import heapq
#     cur_sec = 0  # 현재시간
#     pq = []  # 현재 시간에 작업 대기중인 work
#     result = []  # 각각의 work 당 작업 시간을 저장
#     jobs.sort()  # 작업 투입 시간이 적은 순서대로 정렬
#     length_jobs = len(jobs)
#     idx = 0  # 작업 투입 개수

#     while idx < length_jobs or pq:  # 작업에 모두 투입하고 대기중인 작업도 없으면 종료
#         for i in range(idx, len(jobs)):
#             if jobs[i][0] <= cur_sec:  # 작업에 투입할 시간이 현재시간보다 적으면 투입!!
#                 # 힙큐를 쓰기 위해 작업시간과 투입시간의 순서를 바꿔서 넣어줌
#                 heapq.heappush(pq, [jobs[i][1], jobs[i][0]])
#             else:
#                 idx = i
#                 break
#         else:
#             idx = i + 1

#         print('대기중인 작업: ', pq)

#         if pq:
#             # 작업시간, 투입시간
#             work_sec, enter_sec = heapq.heappop(pq)
#             # cur_sec-enter_sec: 대기시간
#             result.append(work_sec + cur_sec - enter_sec)
#             # 작업시간만큼 현재시간 ++
#             cur_sec += work_sec

#         else:
#             cur_sec += 1
        
#     # 결과
#     print(result, length_jobs)
#     answer = sum(result) // length_jobs
#     return answer

a = solution([[0, 3], [1, 9], [2, 6]])
print(a)
