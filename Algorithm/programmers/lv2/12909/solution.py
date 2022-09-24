def solution(s):
    stack = []
    if s[0] == ')' or s[-1] == '(':
        return False

    for i in s:
        if i == '(': 
            stack.append(i)
        else: 
            if stack == []: 
                return False
            else:
                stack.pop() 
    
    return stack == []