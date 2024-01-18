# 연습문제 멀리뛰기

# 문제 설명
# 효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

# 제한 사항
# n은 1 이상, 2000 이하인 정수입니다.
# 입출력 예
# n	result
# 4	5
# 3	3
# 입출력 예 설명
# 입출력 예 #1
# 위에서 설명한 내용과 같습니다.

# 입출력 예 #2
# (2칸, 1칸)
# (1칸, 2칸)
# (1칸, 1칸, 1칸)
# 총 3가지 방법으로 멀리 뛸 수 있습니다.


# 이거 2개빼고 다 시간초과
def solution(n):
    from itertools import permutations

    answer = 1
    # 2는 최대 n//2개 가 들어갈 수 있음 i는 2의 갯수임
    # 2가 0개일때, 배열의 갯수는 n - 0개, 1의 개수는 n-0개
    #   1, 1, 1, 1, 1
    # 2가 1개 일때 배열의 갯수는 n - 1개, 1의 갯수는 n-(2*1)개
    #   1, 1, 1, 2
    #   1, 1, 2, 1
    #   1, 2, 1, 1
    #   2, 1, 1, 1
    # 2가 2개 일때 배열의 갯수는 n - 2개, 1의 갯수는 n-(2*2)개
    #   1, 2, 2
    #   2, 1, 2
    #   2, 2, 1

    for i in range(0, n // 2 + 1):
        temp = [1] * (n - (2 * i))
        temp.extend([2] * i)
        print()
        # print(list(set(list(permutations(temp, len(temp))))))
        # print(i, n, n // 2, temp)

        # temp = [1] * n - i
        # print(temp)
        # answer += len(list(set(list(permutations(, n - i)))))
        # print(answer)

    return answer


def solution(n):
    if n < 3:
        return n
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n] % 1234567


solution(4)
