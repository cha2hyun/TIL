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



# operations = ["I 16", "D 1"]
# operations = ["I 7", "I 5", "I -5", "D -1"]	
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
o = solution(operations)
print(o)
    