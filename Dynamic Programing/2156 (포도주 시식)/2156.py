n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0]
dp.append(wine[0])
dp.append(wine[0] + wine[1])

for i in range(3, n+1):
    # 경우 1 : 이전 포도주를 먹지 않은 경우
    case_1 = wine[i-1] + dp[i-2]
    
    # 경우 2 : 이전 포도주도 먹은 경우
    case_2 = wine[i-1] + wine[i-2] + dp[i-3]
    
    # 경우 3 : 포도주를 먹지 않아야 하는 경우
    case_3 = dp[i-1]
    
    max_value = max(case_1, case_2, case_3)    
    dp.append(max_value)
    
print(dp[-1])