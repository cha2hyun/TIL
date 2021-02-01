def solution(bridge_length, weight, truck_weights):
    from collections import deque 
    queue = deque()
    queue.append(1)
    print(queue)
    queue.popleft()
    
    answer = 0
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

solution(bridge_length, weight, truck_weights)