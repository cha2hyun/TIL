def solution(n, stations, w):
    from math import ceil
    answer = 0
    # 스테이션이 최대 커버할 수 있는 거리는 왼쪽 w + 오른쪽 w + 본인
    max_range = w + w + 1

    # 시작 위치
    cursor = 1 
    for station in stations:
        # 제공받은 스테이션까지 최소 몇개를 깔아야하는지
        answer += ceil((station - w - cursor) / max_range)
        # 깔았다면 시작 위치 변경
        cursor = station + w + 1
    
    # 기존에 깔린 station 돌은 커서 위치가 전체 길이보다 작을경우 
    if n >= cursor:
        answer += ceil((n - cursor + 1) / max_range)
    
    return answer



    # # 스택을 초기화한다.
    # stack = [1 for i in range(1, n+1)]

    # # 4G 스테이션이 닿는 거리 w만큼 원소를 0으로 바꿔줌
    # for station in stations:
    #     if station == 1:
    #         stack[:station+w] = [0] * (w+1)
    #     elif station == n:
    #         stack[station-w-1:] = [0] * (w+1)
    #     else:
    #         stack[station-w-1 : station+w] = [0] * (w * 2 + 1)
    
    # print(stack)

    # # 스택에서 연속적으로 1이 나오는 갯수를 확인한다.
    # for i in range(len(stack)):


print(solution(11, [3,11], 1))