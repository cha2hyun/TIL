def plusMinus(arr):
    positive = negative = zero = 0
    for number in arr:
        if number == 0:
            zero += 1
        elif number > 0:
            positive += 1
        elif number < 0:
            negative += 1
    print("%.6f" % (positive / len(arr)))
    print("%.6f" % (negative / len(arr)))
    print("%.6f" % (zero / len(arr)))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
