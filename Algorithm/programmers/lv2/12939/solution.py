def solution(s):
    arr = []
    for char in s.split(" "):
        arr.append(int(char))
    answer = str(min(arr)) + " " + str(max(arr))
    return answer


solution("1 2 3 4")


# 다른사람 풀이
def solution(s):
    s = list(map(int, s.split()))
    print(s)
    return str(min(s)) + " " + str(max(s))


# 다른사람 풀이
def solution(s):
    # return str(min([int(i) for i in s.split(' ')])) + ' ' + str(max([int(i) for i in s.split(' ')]))
    pass


# 1월 19일 복기


def solution(s):
    arr = s.split(" ")
    return f"{str(min(arr))} {str(max(arr))}"
