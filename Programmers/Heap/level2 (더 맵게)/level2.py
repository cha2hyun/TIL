def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    result = 0
    
    while len(scoville) >= 2:
        min_1 = heapq.heappop(scoville)
        
        if min_1 >= K:
            return result
        else:
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_1 + (min_2*2))
            result += 1
    if scoville[0] > K:
        return result
    else:
        return -1




# def solution(scoville, K):
#     from collections import deque
#     arr = deque(scoville)
#     cnt = 0
#     while arr[0] < K:
#         if len(arr) == 1:
#             return -1
#         if arr[0] < K:
#             arr[0] = arr[0] + arr[1]*2
#             arr.leftpop(1)
#         arr = list(set(arr))
#         cnt += 1
#     return cnt

scoville = [1, 2, 3, 9, 10, 12]
K = 7

s = solution(scoville, K)
print(s)