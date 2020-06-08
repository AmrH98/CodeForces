#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    for word in s[:].split():
        s = s.replace(word, word.capitalize())
    return s
    
    # final = []
    # for word in s.split():
    #     for i in range(len(word)):
    #         if word[i].isalpha():
    #             final.append(word[0].upper() + word[1:].lower())
    #             print(final)
    #             break
    # return ' '.join(final)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
