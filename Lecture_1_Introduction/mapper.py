#!/usr/bin/python
"""mapper.py"""

import sys

for line in sys.stdin:
    # read an input from the system and remove spaces from the beginning and the end
    line = line.strip()
    #splits the string into words and save it in a list
    words = line.split()
    #print(words)
    #for each word in the list, assign 1 to its count
    for word in words:
        print(f'{word}\t{1}')


