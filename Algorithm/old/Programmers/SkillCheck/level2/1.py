def solution(nums):
    maximum = len(nums) // 2
    minimum = len(set(nums))
    if minimum < maximum : 
        return minimum
    else:
        return maximum
    

a = solution([3,3,3,2,2,2])
print(a)