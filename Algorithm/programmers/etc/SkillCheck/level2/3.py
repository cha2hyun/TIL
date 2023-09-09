from math import comb

# 시도 3
def solution(clothes):
    import itertools

    category = [i[1] for i in clothes]
    combination = list(itertools.combinations(category, 2))
    print(category)
    print(combination)

    return len(category) + len(combination)


# 시도 2
def solution2(clothes):
    import itertools

    category = [i[1] for i in clothes]

    combination = list(itertools.combinations(category, 2))
    answer = len(category) + len(combination)
    for c in combination:
        if c[0] == c[1]:
            answer -= 1

    return answer


# 시도 1
def solution1(clothes):
    closet = {}
    clothType = [i[1] for i in clothes]

    for cloth in clothType:
        if cloth not in closet:
            closet[cloth] = clothType.count(cloth)

    temp = list(closet.values())
    answer = 1
    if len(temp) == 1:
        return temp[0]

    for t in temp:
        answer = answer * t

    for t in temp:
        answer += t

    return answer


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


clothes = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
    # ["yellow_hat", "headgear"],
    # ["blue_sunglasses", "eyewear"],
    # ["green_turban", "headgear"],
    # ["crow_mask", "face"],
    # ["blue_sunglasses", "face"],
    # ["smoky_makeup", "face"],
]


print(solution(clothes))
