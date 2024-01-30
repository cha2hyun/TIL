#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    sorted_grid = []
    for g in grid:
        sorted_grid.append(sorted(list(g)))

    for i in range(len(sorted_grid[0])):
        temp = sorted(sorted_grid, key=lambda x: x[i])
        if temp != sorted_grid:
            return "NO"
    return "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        fptr.write(result + "\n")

    fptr.close()
