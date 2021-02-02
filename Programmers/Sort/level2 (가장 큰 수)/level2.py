def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))
# def solution(numbers):
#     from itertools import permutations
#     arr = [ str(i) for i in numbers]
#     per = permutations(arr, len(arr))
    
#     temp_arr = []
#     for pp in per:
#         temp = ''
#         for p in pp:
#             temp += p
#         temp_arr.append(temp)
    
#     answer = str(max(temp_arr))
    
#     return answer