import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # Cap_Str = s.title()
    # return Cap_Str
    return ' '.join(w.capitalize() for w in s.split(' '))

if __name__ == '__main__':
    fptr = open('file.txt', 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()