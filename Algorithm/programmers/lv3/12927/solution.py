def solution(n, works):
    import heapq
    # 1 음수로 치환하여 heap을 만든다
    works = [-work for work in works]
    heapq.heapify(works)

    # 2~3 작업량을 1 감소시키고 다시 힙에 푸쉬 (n만큼)
    for i in range(n):
        work = heapq.heappop(works)
        heapq.heappush(works, work + 1)
    
    # 4 남은것중 음수인 원소는 앞으로 해야할 야근임
    answer = 0
    for i in works:
        if i < 0:
            answer += i*i
    
    return answer
        

print(solution(4,[4, 3, 3]))