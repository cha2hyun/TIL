def solution(step, start):
    # 예시의 노란색의 합을 arr 배열에 저장한다.
    # arr 배열에서 똑같은 숫자가 나오면 다음번에는 이미 방문한 위치에 도달했다는 것.
    # 따라서 리턴할때는 + 3 을 해줌 (1회차부터 시작, 7회차에 이미 8회차에 도달한다는 것을 아므로
    arr = []
    cursor = start - 1
    cnt = step[cursor]
    while True:
        cursor = cursor + step[cursor]
        next_step = step[cursor]
        cnt += next_step
        if cnt in arr:
            return len(arr) + 3
        else:
            arr.append(cnt)


N = input()
step = list(map(int, input().split()))
result = max(solution(step, 1), solution(step, 2), solution(step, 3))
print(result)