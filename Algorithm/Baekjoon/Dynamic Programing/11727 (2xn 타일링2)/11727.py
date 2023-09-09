# dp(n) = dp(n-1) + 2*dp(n-2)
# 점화식만 세우면 끝

dp = [1,3,5,11]
n = int(input())
for i in range(4,n):
    dp.append(dp[i-1] + (dp[i-2]*2) )

print(dp[-1])