# dp[n] = dp[n-1] + dp[n-2] + dp[n-3] (n>3)

n = int(input())
dp = [0,1,2,4]

for i in range(4, n+1):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

print(dp[-1])