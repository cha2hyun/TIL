def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    
    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        
    return time


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

s = solution(bridge_length, weight, truck_weights)
print(s)


#bridge_length : 2, weight : 10, truck_weights : 7, 4, 5, 6 일때
# bridge는 [0] * 2 = [0, 0] // 현재 다리 길이만큼
# 트럭이 다리를 건널 때 [0, 7] -> [7, 0] -> [0, 4]… 다리가 버틸 수 있는 무게를 체크하고, 초마다 한칸씩 pop하여 이동시킵니다.
# 무게를 초과했을 경우에는 0을 추가해주며 모든 트럭이 다 건넌 후의 경과 시간을 출력합니다.