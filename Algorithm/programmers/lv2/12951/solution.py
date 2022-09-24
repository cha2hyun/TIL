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
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    answer=' '.join(s)
    return answer

solution("3people unFollowed me")