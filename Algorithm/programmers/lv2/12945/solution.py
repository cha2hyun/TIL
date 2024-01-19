def solution(n):
    fabo = [None] * (n + 1)
    fabo[0] = 0
    fabo[1] = 1
    for i in range(n + 1):
        if i < 2:
            pass
        else:
            fabo[i] = (fabo[i - 1] + fabo[i - 2]) % 1234567
    print(fabo)
    return fabo[n]


# print(solution(5))


# 1월 19일 복기


def solution(n):
    dp = [None] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[-1] % 1234567


print(solution(6))


def fibonacci(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, (a + b) % 1234567
        print(a, b)
    return a


fibonacci(6)
