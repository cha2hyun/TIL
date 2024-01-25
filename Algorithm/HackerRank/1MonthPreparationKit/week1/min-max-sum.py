def array_sum(arr):
    temp = 0
    for i in arr:
        temp += i
    return temp


def miniMaxSum(arr):
    arr = sorted(arr)
    print(array_sum(arr[0:4]), array_sum(arr[len(arr) - 4 :]))

    # Write your code here


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
