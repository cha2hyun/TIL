def solution(triangle):
    
    triangle = [[0] + line + [0] for line in triangle]
    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])    
    return max(triangle[-1])
    



triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)
# result = 30

