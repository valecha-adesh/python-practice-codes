#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum_d1 = 0
    sum_d2 = 0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i==j:
                sum_d1 = sum_d1 + arr[i][j]

            if (i + j == (len(arr) - 1)):
                sum_d2 = sum_d2 + arr[i][j]

    return abs (sum_d1 - sum_d2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
