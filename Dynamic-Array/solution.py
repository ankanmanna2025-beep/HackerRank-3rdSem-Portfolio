#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Initialize the 2D array with n empty arrays
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    
    # Process each query
    for q in queries:
        query_type = q[0]
        x = q[1]
        y = q[2]
        
        # Calculate the index using the XOR (^) and modulo (%) operators
        idx = (x ^ lastAnswer) % n
        
        if query_type == 1:
            # Query type 1: Append y to arr[idx]
            arr[idx].append(y)
        elif query_type == 2:
            # Query type 2: Find the value, assign it to lastAnswer, and store it
            size = len(arr[idx])
            lastAnswer = arr[idx][y % size]
            answers.append(lastAnswer)
            
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
