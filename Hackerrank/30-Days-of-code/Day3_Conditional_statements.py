#!/bin/python3

import math
import os
import random
import re
import sys


def func(N):
    if N%2==0:
        if N>=2:
            if N<=5:
                print("Not Weird")
            elif N<=20:
                print("Weird")
            else:
                print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    N = int(input())

    func(N)
