from itertools import combinations

def solution(relation):
    answer = 0

    combination = []
    for cnt in range(1, len(relation[0]) + 1):
        combination.append(list(combinations(temp, cnt)))
        
    return answer


relation = [
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]

print(solution(relation))