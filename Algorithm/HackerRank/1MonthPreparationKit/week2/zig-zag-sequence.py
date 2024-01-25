"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given an array of  distinct integers, transform the array into a zig zag sequence by permuting the array elements. A sequence will be called a zig zag sequence if the first  elements in the sequence are in increasing order and the last  elements are in decreasing order, where . You need to find the lexicographically smallest zig zag sequence of the given array.

Example.


Now if we permute the array as , the result is a zig zag sequence.

Debug the given function findZigZagSequence to return the appropriate zig zag sequence for the given input array.

Note: You can modify at most three lines in the given code. You cannot add or remove lines of code.

To restore the original code, click on the icon to the right of the language selector.

Input Format

The first line contains  the number of test cases. The first line of each test case contains an integer , denoting the number of array elements. The next line of the test case contains  elements of array .

Constraints


 ( is always odd)

Output Format

For each test cases, print the elements of the transformed zig zag sequence in a single line.
https://velog.io/@sage_ai/HackerRank-Zig-Zag-Sequence-Python3
"""


def findZigZagSequence(a, n):
    a.sort()
    mid = int(n / 2)  # modified
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2  # modified
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1  # modified

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")
    return


test_cases = int(input())
for cs in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
