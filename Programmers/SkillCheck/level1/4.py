def solution(n):
    import math
    sqrt = math.sqrt(n)
    
    if sqrt % 1 == 0:
        return int(sqrt + 1) * int(sqrt + 1)
    else:
        return -1
    

n = solution(121)
print(n)