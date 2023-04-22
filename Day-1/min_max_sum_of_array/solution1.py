#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minimum = maximum = 0
    if all(x == arr[0] for x in arr):
        new_arr = arr[:-1]
        minimum = maximum = sum (new_arr)
        return print(f"{minimum} {maximum}")
    else:
        for num in [x for x in arr if x != min(arr)]:
            maximum += num
        for num in [x for x in arr if x != max(arr)]:
            minimum += num
        return print(f"{minimum} {maximum}")
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
