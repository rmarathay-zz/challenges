#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def handles_everything_am(s):
    if s[:2] == '12':
        if s == '12:00:00AM':
            return  '00:00:00'
        else:
            military_time = '00' + s[2:-2]
            return military_time
    else:
        military_time = s[:-2]
        return military_time
        
    
def handles_everything_pm(s):
    if s[:2] == '12':
        if s == '12:00:00PM':
            return  '12:00:00'
        else:
            military_time = s[:-2]
            return military_time
    else:
        old_hour = int(s[:2])
        military_time = str(old_hour + 12) + s[2:-2]
        return military_time

    
def timeConversion(s):        
    if s[-2:] == 'AM':
        return handles_everything_am(s)
        
    if s[-2:] == 'PM':
        return handles_everything_pm(s)


if __name__ == '__main__':
    
    tests = [
        ('12:15:15AM', '00:15:15'),
        ('12:59:59AM', '00:59:59'),
        ('06:45:10AM', '06:45:10'),
        ('12:40:30PM', '12:40:30'),
        ('01:40:30PM', '13:40:30'),
        ('08:08:58PM', '20:08:58'),
        ('01:15:50AM', '01:15:50'),
    ]

    for input, expected in tests:
        t = timeConversion(input)
        print(t)
        assert(t == expected)
        
