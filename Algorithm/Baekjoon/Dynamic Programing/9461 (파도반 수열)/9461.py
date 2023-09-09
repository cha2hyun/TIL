# 점화식을 찾으면됨
# n     = 1  2  3  4  5  | 6  7  8  9  10  11  12
# dp(n) = 1  1  1  2  2  | 3  4  5  7  9   12  16
# n = 6번부터 보면 규칙을 볼 수 있음
# 점화식 dp(n) = dp(n-1) + dp(n-5)

dp = [1,1,1,2,2]
n = int(input())
for i in range(5,n):
    dp.append(dp[i-1] + dp[i-5] )

print(dp[-1])