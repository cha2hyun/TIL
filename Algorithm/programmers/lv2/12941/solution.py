# def comp(A, B, length):
#     X = []
#     Y = []
#     X = X.extend(A)
#     Y = Y.extend(B)
#     total = 0
#     for i in range(length):
#         Max = max(X)
#         Min = min(Y)
#         X.remove(Max)
#         Y.remove(Min)
#         total += Max * Min
#     return total

# def solution(A, B):
#     length = len(A)
#     total = 0

#     for i in range(length):
#         Max = max(A)
#         Min = min(B)
#         A.remove(Max)
#         B.remove(Min)
#         total += Max * Min
# return total


def solution(A, B):
    total = 0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        total += A[i] * B[i]
    return total


solution([1, 4, 2], [5, 4, 4])
