def solution(arr):
    cnt = 0
    while True:
        if len(arr) == 1:
            break
        
        half = len(arr)//2
        left = arr[:half]
        right = arr[half:]

        if max(left) > max(right):
            arr = right
            cnt += max(left)
        else:
            arr = left
            cnt += max(right)
        
    return cnt

arr = [1, 3, 10, 9, 6, 2, 3, 2]
print(solution(arr))