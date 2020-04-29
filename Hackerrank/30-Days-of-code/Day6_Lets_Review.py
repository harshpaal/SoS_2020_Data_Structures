# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    for i in range(0,n,1):
        string = str(input())
        even = ""
        odd = ""
        num=0
        for x in string:
            if num%2==0:
                even+=x
            else:
                odd+=x
            num+=1
        print(even+" "+odd)
