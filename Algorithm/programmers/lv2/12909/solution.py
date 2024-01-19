def solution1(s):
    stack = []
    if s[0] == ")" or s[-1] == "(":
        return False

    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()

    return stack == []


# 1월 19일 복기


def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(0)
        elif s[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False


solution("(())()")
solution(")()(")
