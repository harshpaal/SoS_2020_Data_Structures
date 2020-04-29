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
    # Write your code here
    lastAns=0
    return_ans=[]
    seqList=[]
    for ind in range(0,n,1):
        seqList.append([])

    for index in range(0,len(queries),1):
        x=queries[index][1]
        y=queries[index][2]
        if queries[index][0]==1:
            seqList[(x^lastAns)%n].append(y)
        
        if queries[index][0]==2:
            seq=seqList[(x^lastAns)%n]
            lastAns = seq[y%len(seq)]
            return_ans.append(lastAns)
    return return_ans
    
            

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
