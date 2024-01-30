"""
Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.

Example


 is between two subarrays that sum to .


The answer is  since left and right sum to .

You will be given arrays of integers and must determine whether there is an element that meets the criterion. If there is, return YES. Otherwise, return NO.

Function Description

Complete the balancedSums function in the editor below.

balancedSums has the following parameter(s):

int arr[n]: an array of integers
Returns

string: either YES or NO
Input Format

The first line contains , the number of test cases.

The next  pairs of lines each represent a test case.
- The first line contains , the number of elements in the array .
- The second line contains  space-separated integers  where .

Constraints





Sample Input

2
3
1 2 3
4
1 2 3 3
Sample Output

NO
YES
Explanation

For the first test case, no such index exists.
For the second test case, , therefore index  satisfies the given conditions.
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def balancedSums(arr):
    # arr > [0, .. , i]
    # arr [o] .. [i] .. [-1-i] .. [-1]
    # arr [0], [-1] exeception
    # arr [i:] ~ [-1-i]
    # if sum(arr[:i]) == sum(arr[i+1:])
    #   return "YES"
    # else return "NO"

    # exception case
    # [first index, 0, 0, .. 0, 0]
    # [0, 0, .. 0, 0, last index]
    if sum(arr[1:]) == 0 or sum(arr[:-1]) == 0:
        return "YES"

    # main logic
    start = 1
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        leftSum = sum(arr[:mid])
        rightSum = sum(arr[mid + 1 :])
        if leftSum == rightSum:
            return "YES"
        elif leftSum > rightSum:
            end = mid - 1
        else:
            start = mid + 1
    return "NO"

    # for i in range(1, len(arr)-1):
    #     if sum(arr[:i]) == sum(arr[i+1:]):
    #         return "YES"
    # return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + "\n")

    fptr.close()
