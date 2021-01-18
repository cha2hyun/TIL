import sys

n = int(sys.stdin.readline())

# N x 3 DP Table 생성
# table[i][0] = i번째 집을 빨강으로 칠하는 경우
# table[i][1] = i번째 집을 파랑으로 칠하는 경우
# table[i][2] = i번째 집을 초록으로 칠하는 경우

table = [[0,0,0] for _ in range(n)]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        table[0] = temp
    else:
        # 점화식을 통한 DP Table 채우기
        table[i][0] = min(table[i - 1][1], table[i - 1][2]) + temp[0]
        table[i][1] = min(table[i - 1][0], table[i - 1][2]) + temp[1]
        table[i][2] = min(table[i - 1][0], table[i - 1][1]) + temp[2]
        
# 빨강, 초록, 파랑으로 칠하는 경우 중 최소값 출력
print(min(table[n - 1]))