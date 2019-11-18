#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(s):
    result = []
    start = 0
    for i in s:
        if i == 'U':
            start += 1
        else:
            start -= 1
        result.append(start)
    count = 0
    climb = 0
    print(result)
    for i in result:
        if i > 0:
            climb = 1
        if climb == 1 and i == 0:
            count += 1
            climb = 0
    return count


s = 'DDUUDDUDUUUD'
print(countingValleys(s))