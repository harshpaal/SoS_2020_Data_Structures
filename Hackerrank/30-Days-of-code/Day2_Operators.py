#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tax1 = meal_cost*(float(tip_percent)/100)
    tax2 = meal_cost*(float(tax_percent)/100)
    return meal_cost+tax1+tax2

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(round(solve(meal_cost, tip_percent, tax_percent)))
