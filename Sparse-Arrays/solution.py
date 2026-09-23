#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    # Use a dictionary to store the frequency of each string in stringList
    frequency_map = {}
    
    for string in stringList:
        if string in frequency_map:
            frequency_map[string] += 1
        else:
            frequency_map[string] = 1
            
    # Look up the count for each query
    result = []
    for query in queries:
        if query in frequency_map:
            result.append(frequency_map[query])
        else:
            result.append(0)
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
