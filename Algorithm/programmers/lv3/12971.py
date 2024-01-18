def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    answer = 0
    # 첫 번째 선택
    dp1 = [0 for _ in range(len(sticker))]
    dp1[0], dp1[1] = sticker[0], sticker[0]

    # 첫 번째를 선택하지 않았을 경우
    dp2 = [0 for _ in range(len(sticker))]
    dp2[0], dp2[1] = 0, sticker[1]

    print(dp1)
    # [14, 14, 0, 0, 0, 0, 0, 0]

    print(dp2)
    # [0, 6, 0, 0, 0, 0, 0, 0]

    for i in range(2, len(sticker)):
        if i == len(sticker) - 1:
            dp2[i] = max(dp2[i - 1], sticker[i] + dp2[i - 2])
        else:
            dp1[i] = max(dp1[i - 1], sticker[i] + dp1[i - 2])
            dp2[i] = max(dp2[i - 1], sticker[i] + dp2[i - 2])
        print(i, dp1, dp2)
        # 2 [14, 14, 19, 0, 0, 0, 0, 0]       [0, 6, 6, 0, 0, 0, 0, 0]
        # 3 [14, 14, 19, 25, 0, 0, 0, 0]      [0, 6, 6, 17, 0, 0, 0, 0]
        # 4 [14, 14, 19, 25, 25, 0, 0, 0]     [0, 6, 6, 17, 17, 0, 0, 0]
        # 5 [14, 14, 19, 25, 25, 34, 0, 0]    [0, 6, 6, 17, 17, 26, 0, 0]
        # 6 [14, 14, 19, 25, 25, 34, 34, 0]   [0, 6, 6, 17, 17, 26, 26, 0]
        # 7 [14, 14, 19, 25, 25, 34, 34, 0]   [0, 6, 6, 17, 17, 26, 26, 36]

    answer = max(dp1[len(dp1) - 2], dp2[len(dp2) - 1])

    return answer


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
