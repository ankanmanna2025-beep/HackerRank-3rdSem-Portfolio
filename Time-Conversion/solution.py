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
    period = s[-2:]
    time_parts = s[:-2].split(':')
    
    hour = int(time_parts[0])
    minute = time_parts[1]
    second = time_parts[2]
    
    if period == 'AM':
        if hour == 12:
            hour = 0
    else: # PM
        if hour != 12:
            hour += 12
            
    return f"{hour:02d}:{minute}:{second}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
