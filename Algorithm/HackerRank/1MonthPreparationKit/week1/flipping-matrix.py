def matrix_sum(matrix):
    answer = 0
    half = len(matrix) // 2
    for i in range(half):
        answer += sum(matrix[i][0:half])
    return answer


def reverse(direction, matrix, idx):
    matrix = matrix.copy()
    if direction == "row":
        matrix[idx] = matrix[idx][::-1]
    elif direction == "col":
        for j in range(len(matrix) // 2):
            temp = matrix[j][idx]
            matrix[j][idx] = matrix[len(matrix) - j - 1][idx]
            matrix[len(matrix) - j - 1][idx] = temp
    return matrix


def flippingMatrix(matrix):
    answer = 0
    for i in range(len(matrix)):
        arr = 0
        for j in range(len(matrix)):
            arr = reverse("row", matrix, j)
        arr = reverse("col", arr, i)
        answer = max(answer, matrix_sum(arr))
        print(answer)

    for i in range(len(matrix)):
        arr = 0
        for j in range(len(matrix)):
            arr = reverse("col", matrix, j)
        arr = reverse("row", arr, i)
        answer = max(answer, matrix_sum(arr))

    return answer


arr = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(flippingMatrix(arr))


"""
https://hee0.tistory.com/18
DP 를 이용하면된다
총길이가 2n x 2n 일때 n x n의 합을 구하는것임
0,0 에 올수있는 최대치는 (0,0) (0,2n) (2n,0) (2n,2n) 의 최대값 
0,1 에 올수있는 최대치는 (0,1) (0,2n-1), (2n-1,0), (2n-1,2n-1) 중 최대값 

행과열을 각각 i, j 라고 할 때, n x n 행렬의 가장 큰 값은
(i, j) (i, n-j) (n-i, j) (n-i, n-j) 에 위치한 값 중 큰 값

(n,n) (n, 2n-(n+1)) (2n-(n+1), n) (2n-(n+1), 2n-(n+1))
dp => max(A[i][j], A[2 * n - 1 - i][j], A[i][2 * n - 1 - j], A[2 * n - 1 - i][2 * n - 1 - j])

"""
# for i in range(n):
#     for j in range(n):
#         ans += max(A[i][j], A[2 * n - 1 - i][j], A[i][2 * n - 1 - j], A[2 * n - 1 - i][2 * n - 1 - j])
