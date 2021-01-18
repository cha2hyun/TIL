# dp[n] = dp[n-2] + dp[n-1]
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 5


dp = [0,1,2,3]
n = int(input())
for i in range (4, n+1):
    dp.append(dp[i-2] + dp[i-1])

print(dp[-1])