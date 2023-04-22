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
    minimum = maximum = sum(arr)
    if len(set(arr)) == 1:
        minimum = maximum = sum(arr[:-1])
    else:
        minimum -= max(arr)
        maximum -= min(arr)
    return print(f"{minimum} {maximum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
