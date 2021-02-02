def solution(arr):
    if len(arr) == 1:
        return [-1]
    print(min(arr))
    answer = arr
    print(answer)
    answer.remove(min(answer))
    print(answer)
    return answer 

a = solution([4,3,2,1])
print(a)

b = [3,4]
b.remove(3)
print(b)