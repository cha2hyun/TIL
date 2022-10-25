def solution(s):
    stack = []
    for i in range(len(s)):
        print(stack)
        if not stack:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
    if stack:
        return 0
    else:
        return 1

    # while True:
    #     cnt = 0
    #     length = length
    #     for i in range(0, length - 1):
    #         cnt += 1
    #         if s[i] == s[i+1]:
    #             s = s[:i] + s[i+2:]
    #             break
    #     if s == '':
    #         return 1
    #     elif cnt > len(s)/2:
    #         return 0

        
print(solution("baabaa"))