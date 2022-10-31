def get_small_pocket(arr1, arr2):
    if arr1[1] - arr1[0] > arr2[1] - arr2[0]:
        return arr2
    return arr1


def solution(gems):
    from collections import defaultdict
    target = len(set(gems))
    answer = [0, len(gems)]
    pocket = defaultdict(int)
    start, end = 0, 0

    while end < len(gems):
        pocket[gems[end]] += 1 
        end += 1
        if len(pocket) == target:
            while start < end:
                if pocket[gems[start]] > 1:
                    pocket[gems[start]] -= 1
                    start += 1
                else:
                    answer = get_small_pocket(answer, [start + 1, end])
                    break
   
    return answer


            
            

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))