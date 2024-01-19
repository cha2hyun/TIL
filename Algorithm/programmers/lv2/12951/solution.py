# def solution(s):
#     answer = ''
#     arr = s.split(" ")
#     for string in arr:
#         if string[0].isalpha():
#             answer += string.title() + " "
#         else:
#             answer += string + " "
#     return answer[:-1]


# def solution(s):
#     answer = ''
#     flag = True
#     for char in s:
#         if char.isdigit():
#             answer += char
#             flag = False
#         elif flag:
#             answer += char.upper()
#             flag = False
#         elif char == " ":
#             answer += " "
#             flag = True
#         else:
#             answer += char.lower()
#     return answer


def solution(s):
    answer = ""
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    answer = " ".join(s)
    return answer


def solution(s):
    answer = ""
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    answer = " ".join(s)
    return answer


# 1월 19일 복기로 다시 풀어봄


def solution1(s):
    answer = ""
    arr = s.split(" ")
    for word in arr:
        answer += f"{word.capitalize()} "
    return answer[:-1]


def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()


solution1("3people unFollowed me")
