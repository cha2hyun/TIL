# def solution(clothes):    
#     dic = {}
#     for cloth in clothes:
#         if cloth[1] not in dic:
#             dic[cloth[1]] = 0    
#         dic[cloth[1]] += 1
        
#     if len(dic) == 1:
#         return list(dic.values())[0]

#     for k in dic:
#         answer *= dic[k] + 1

#     return answer - 1
    
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y+1), cnt.values(), 1) - 1
    return answer



clothes = [
    ["crow_mask", "face"], 
    ["blue_sunglasses", "face"], 
    ["smoky_makeup", "face"],
    # ["yellow_hat", "headgear"],
    # ["green_turban", "headgear"],
    # ["blue_sunglasses", "eyewear"]
]
a = solution(clothes)
print(a)