def jump(stones, k, mid):
    cnt = k
    for stone in stones:
        if stone <= mid:
            cnt -= 1
            if cnt == 0:
                return False
        else:
            cnt = k
    return True

def solution(stones, k):
    # stones배열 각 원소들의 값은 1이상 200만 이하의 자연수
    # max(stones)는 200만이 될 수도 있음
    answer, left, right = 0, 1, max(stones)
    
    # left가 right 되면 반복문을 멈춘다.
    while left <= right:
        # 중간값
        mid = (left + right) // 2
        print("left", left, "right", right, "mid", mid)
        # 만약에 점프가 된다면 
        if jump(stones, k, mid):
            print(">> 여기서 점프됨 !!")     
            # left 에 mid + 1    
            answer = left = mid + 1
        # 안되면
        else:
            # right 에 mid - 1
            right = mid - 1      
    print(answer, "리턴합니다")
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) #3

