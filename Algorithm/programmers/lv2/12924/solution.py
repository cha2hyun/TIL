def factorial(n):
    ret = 0
    for i in range(1, n + 1):
        ret += i
    return ret


def solution1(n):
    answer = 0
    flag = False
    for x in range(1, (n + 1)):
        temp = 0
        for y in range(x, (n + 1) // 2 + 1):
            print(flag, y, temp, answer)
            if flag:
                flag = False
                break
            temp += y
            if temp == n:
                answer += 1
                flag = True
                break
            elif temp > n:
                break
        print(" ")
    return answer + 1


def solution(n):
    answer = 0
    for i in range(1, n + 1, 2):
        if n % i == 0:
            answer += 1
    return answer


print(solution(15))
