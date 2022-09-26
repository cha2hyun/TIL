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
    return fabo[n - 1]


print(solution(5))
