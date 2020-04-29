#!/bin/python3

import math
import os
import random
import re
import sys

def find_one(string, m, state):
    if m==len(string)-1:
        return state
    if string[m+1]==1:
        return find_one(string, m+1, state+1)
    else:
        return state

def num_cons(string):
    max_num=0
    for i in range(len(string)):
        if string[i]==1:
            max_num=max(max_num, find_one(string, i, 1))
    return max_num


if __name__ == '__main__':
    x = int(input())
    binary_n = list()
    while (x!=0):
        binary_digit = x%2
        binary_n.append(binary_digit)
        x//=2

    print(num_cons(binary_n))
    
