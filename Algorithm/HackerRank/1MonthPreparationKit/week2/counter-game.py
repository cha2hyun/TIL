"""
Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of . If it is, they divide it by . If not, they reduce it by the next lower number which is a power of . Whoever reduces the number to  wins the game. Louise always starts.

Given an initial value, determine who wins the game.

Example

It's Louise's turn first. She determines that  is not a power of . The next lower power of  is , so she subtracts that from  and passes  to Richard.  is a power of , so Richard divides it by  and passes  to Louise. Likewise,  is a power so she divides it by  and reaches . She wins the game.

Update If they initially set counter to , Richard wins. Louise cannot make a move so she loses.

Function Description

Complete the counterGame function in the editor below.

counterGame has the following parameter(s):

int n: the initial game counter value
Returns

string: either Richard or Louise
Input Format

The first line contains an integer , the number of testcases.
Each of the next  lines contains an integer , the initial value for each game.

Constraints

Sample Input

1
6
Sample Output

Richard
Explanation

As  is not a power of , Louise reduces the largest power of  less than  i.e., , and hence the counter reduces to .
As  is a power of , Richard reduces the counter by half of  i.e., . Hence the counter reduces to .
As we reach the terminating condition with , Richard wins the game.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def counterGame1(n):
    # Write your code here
    # power_of_2 = [1, 2, 4, 8, ... , 2^64] while n > power_of_2
    # cnt = 0

    # initialization
    power_of_2 = [1]
    while n > power_of_2[-1]:
        power_of_2.append(2 * power_of_2[-1])

    # main logic
    cnt = 0
    while n != 1:
        if n in power_of_2:
            n = n // 2
        else:
            for i in range(len(power_of_2)):
                if n < power_of_2[i]:
                    n = n - power_of_2[i - 1]
        cnt += 1

    if cnt % 2 == 0:
        return "Richard"
    return "Louise"


def isPowerOf2(number):
    if list(set(bin(number)[3:])) == ["0"]:
        return True
    return False


def counterGame(n):
    cnt = 0
    while n != 1:
        m = bin(n)[2:]
        if list(set(m[1:])) == ["0"]:
            n = n // 2
        else:
            for i in range(1, len(m)):
                if m[i] != 0:
                    n = m[i:]
                    break
            n = int(n, 2)
        cnt += 1

    if cnt % 2 == 0:
        return "Richard"
    return "Louise"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + "\n")

    fptr.close()
