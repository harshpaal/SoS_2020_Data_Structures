#!/bin/python3

import math
import os
import random
import re
import sys

def left_rot(n, d, a):
    return_a = [0]*len(a)
    for ind in range(0,d,1):
        return_a[len(a)-d+ind] = a[ind]

    for ind in range(d,len(a),1):
        return_a[ind-d] = a[ind]
    return return_a



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    result = left_rot(n, d, a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
