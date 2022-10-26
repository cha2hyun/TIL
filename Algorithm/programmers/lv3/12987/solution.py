def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    answer = 0
    # 이렇게 하면 안됨
    # for i in range(len(A)):
    #     if A[i] < B[i]:
    #         answer += 1
    i = 0
    for a in A:
        # B의 원소가 더 클때만 다음 B의 원소를 비교할 것
        if a < B[i]:
            answer += 1
            i += 1
    return answer

print(solution([5,1,3,7],[2,2,6,8]))
