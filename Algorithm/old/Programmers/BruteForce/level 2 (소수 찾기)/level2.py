# 첫번째 제출 정확성 75
# def solution(numbers):
#     import itertools
#     num = [numbers[i] for i in range(len(numbers))]
#     comb_num = []
#     for i in range(1, len(num) + 1):
#         add = list(map(''.join, itertools.permutations(num, i))) 
#         for j in range (len(add)):
#             comb_num.append(add[j])

#     comb_num = list(set(comb_num))
#     answer = 0
#     for idx, n in enumerate(comb_num):
#         if n[0] == '0':
#             continue
#         if isPrime(int(n)) == True:
#             answer += 1    
#     return answer

# 2번째 답안, 1번에서 정확성이 떨어지는건 isPrime 함수 속도떄문 
def solution(numbers):
    import itertools
    import math
    num = [numbers[i] for i in range(len(numbers))]
    comb_num = []

    for i in range(1, len(num) + 1):
        add = list(map(''.join, itertools.permutations(num, i))) 
        for j in range (len(add)):
            comb_num.append(add[j])

    comb_num = list(map(int, comb_num))
    comb_num = list(set(comb_num))  
            
    print(comb_num)
    answer = 0
    for n in comb_num:
        if isPrime(n) == True:
            answer += 1    
    return answer


# 정확성 75점
# def isPrime(number):
#     if number < 2:
#         return False
#     for i in range(2, number):
#         if i * i >= number:
#             break                
#         if number % i == 0:
#             return False
#     return True


# 성공
def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

numbers = "003"


