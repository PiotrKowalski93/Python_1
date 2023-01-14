import math
import os
import random
import re
import sys


def saveThePrisoner(n, m, s):
    last = 0
    
    if m%n == 0 and s == 1:
        return n

    if m < n:
        last = s + m - 1
        if last > n:
            last = last - n
    else:
        x = m%n
        last = (s + x) - 1
        if last > n:
            last = last - n
    
    return last
        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = 100

    with open("Input.txt", 'r') as f:
        for line in f:
            n, m, s = map(int, line.rstrip().split(" "))
            result = saveThePrisoner(n, m, s)
            print(result)
