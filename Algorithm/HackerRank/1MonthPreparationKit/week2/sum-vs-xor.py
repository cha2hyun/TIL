#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def sumXor1(n):
    answer = []
    if n == 0:
        return 1

    for i in range(n):
        if n ^ i == n + i:
            answer.append(i)

    return len(answer)


def sumXor(n):
    # 규칙찾기
    return 1 if n == 0 else 2 ** (bin(n).count("0") - 1)

    # Write your code here


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + "\n")

    fptr.close()
