def solution(m, n, puddles):
    # 점화식 : dp[x][y] = dp[x-1][y] + dp[x][y-1]
    # dp 초기화, 1,1 부터 시작할거고 왼쪽과 위에값을 비교해야하므로 0으로 빈값을 초기화시켜줌
    dp = [[0] * (m+1) for i in range(n+1)]
    # 시작위치
    dp[1][1] = 1
    # 웅덩이는 -1
    for x, y in puddles:
        dp[y][x] = -1
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            # 웅덩이면 0으로 바꿔서 다음값이 위에값이 될 수 있게
            if dp[x][y] == -1:
                dp[x][y] = 0 
                continue                
            # 점화식
            dp[x][y] += dp[x-1][y] + dp[x][y-1]
            # print(dp)

    return dp[n][m] % 1000000007

print(solution(4,3,[[2, 2]]))