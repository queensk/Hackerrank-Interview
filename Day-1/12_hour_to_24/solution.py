#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s.split(':')
    hours = int(time[0])
    minutes = time[1]
    seconds = time[2][:2]
    if s[-2:] == "PM" and hours != 12:
        hours +=12
    elif s[-2:] == "AM" and hours == 12: 
        hours = 0
    return f'{hours:02d}:{minutes:s}:{seconds:s}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
