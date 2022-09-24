# 계단은 한칸 또는 두칸 오를 수 있음
# 연속된 세계의 계단을 밟으면 안된다 -> 두번을 한칸 올랐으면 무조건 그다음엔 두칸을 올라가야함
# 마지막 도착 계단은 반드시 밟아야함 -> 뒤에서 부터 풀이
# 마지막 계단은 밟아야하니 전단계는 -1 계단 혹은 -2 계단

# dp(n) = n칸까지 올랐을때 얻을 수 있는 최대 score
# dp(n) = max(1칸전 에서 올라온 경우, 2칸전 에서 올라온 경우)
# 1칸전에서 올라온 경우 = score[n] + score[n-1] + dp(n-3)  
# --> 연속으로 세번 밟을 수 없으니 직전칸에서 올라온 경우는 n-3 / n-1 / n 이 된다. 
# --> 따라서 n, n-1 의 스코어 점수와 dp(n-3)을 합치면 된다.
# 2칸전에서 올라온 경우 = score(n) + dp[n-2]
# dp(n) = max(score[n] + score[n-1] + dp(n-3), score(n) + dp[n-2] )


import sys 
input = sys.stdin.readline 
score = [] 
n = int(input().strip()) 
for _ in range(n): 
    score.append(int(input().strip()))

dp = []
dp.append(score[0])
for i in range(1, 3):
    if i == 1:
        dp.append(max(dp[i-1] + score[i], score[i]))
        continue
    dp.append(max(dp[i-2] + score[i], score[i-1] + score[i]))

for i in range(3, n): 
    dp.append(max(score[i] + score[i-1] + dp[i-3], score[i] + dp[i-2]))

print(dp[-1])

