"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
Example
Return '12:01:00'.
Return '00:01:00'.
Function Description
Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
timeConversion has the following parameter(s):
string s: a time in  hour format
Returns
string: the time in  hour format
Input Format
A single string  that represents a time in -hour clock format (i.e.:  or ).
Constraints
All input times are valid
Sample Input
07:05:45PM
Sample Output
19:05:45
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # s가 AM인지 PM인지 확인한다 -> isAM = s[-2:] == 'AM
    # s의 AM, PM은 없앤다
    # s를 :로 split 한다. -> 07:05:45PM -> [07,05,45]
    # AM이면 그대로
    # PM이면 12시간을 더해준다
    # AM PM 시간이 12 일때 예외처리를 해주는게 관건인 문제

    isPM = s[-2:] == "PM"
    time = s[:-2].split(":")
    if isPM:
        if time[0] != "12":
            time[0] = int(time[0]) + 12
            if time[0] < 10:
                time[0] = "0" + str(time[0])
            time[0] = str(time[0])
    else:
        if time[0] == "12":
            time[0] = "00"

    print(":".join(time))
    return ":".join(time)


timeConversion("07:05:45PM")
timeConversion("07:05:45AM")
