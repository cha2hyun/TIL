def solution(operations):
    import heapq
    heap = []

    for i in range(len(operations)):
        alphabet, number = operations[i].split(" ")
        if alphabet == "I":
            heapq.heappush(heap, int(number))
        elif alphabet == "D" and heap:
            if number == "1":
                heap.remove(max(heap))
            elif number == "-1":                 
                heapq.heappop(heap)
    
    if heap:
        return [ max(heap), heap[0] ]
    else:
        return [0,0]