#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    string_len = len(strings)
    query_len = len(queries)
    query_ans =[0]*query_len

    for ind in range(0,query_len,1):
        for string in strings:
            if queries[ind]==string:
                query_ans[ind]+=1
    return query_ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
