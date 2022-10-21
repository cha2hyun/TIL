def solution(n, s):
    quotient, remainder = divmod(s, n)
    answer = [quotient] * n
    if n > s:
        return [-1]
    
    for i in range(remainder):
        answer[-i -1] += 1
        
    return answer
            

    # print(f's={s} n={n} s//n={s//n} s%n={s%n}')
    # if(s % n == 0):
    #     return [s // n] * n
    # elif(s % n != 0):
    #     print(s//n)
        

print(solution(2,9))