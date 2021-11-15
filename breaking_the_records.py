#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    i = 0
    min = scores[i]
    max = scores[i]
    low_record = 0
    high_record = 0
    while i < len(scores):
        if scores[i] < min:
            min = scores[i]
            low_record += 1
        if scores[i] > max:
            max = scores[i]
            high_record += 1
        i+=1
    return [high_record, low_record]

if __name__ == '__main__':

    test_cases = [
        ([12,24,10,24], [1,1]),
        ([4,5,0,0,1], [1,1]),
        ([2,2,2,2,2], [0,0]),
    ]

    for input, expected in test_cases:
        result = breakingRecords(input)
        print(result)
        assert(result == expected)