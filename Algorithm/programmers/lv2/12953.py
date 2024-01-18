# 코딩테스트 연습
# 연습문제
# N개의 최소공배수

# N개의 최소공배수
# 문제 설명
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.
# 입출력 예
# arr	result
# [2,6,8,14]	168
# [1,2,3]	6


def solution(arr):
    from math import lcm, gcd

    answer = 1
    # python 3.9 이상 프로그래머스에서는 3.8 사용으로 math의 lcm 사용이 불가함
    # for i in arr:
    #     answer = lcm(answer, i)

    # python 3.9 미만
    for i in arr:
        answer = answer * i // gcd(answer, i)
    return answer


solution([2, 6, 8, 14])
