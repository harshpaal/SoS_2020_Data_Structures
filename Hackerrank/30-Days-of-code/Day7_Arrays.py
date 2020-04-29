#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    brr=[1]*n

    for i in range(0,n,1):
        brr[n-1-i]=arr[i]
    
    print(' '.join(map(str, brr)))
