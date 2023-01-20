#!/usr/bin/python
"""reducer.py"""

import sys

#initialize variables
previous_word = None
previous_count = 0

#for each line in system input (output from map)
c = 0
for line in sys.stdin:
    print(f'Starting Iteration {c}')
    # splits into words
    line = line.strip()
    # now, since we used tab to separate the key from the values in the mapper, we split it using tab separator
    # the first value goes to the word, and the second value goes to the count
    print(f'Line: {line}')
    word, count = line.split('\t')
    print(f'Current word: {word}, Current Count {count}')
    #we convert the count to int
    count=int(count)
    
    if previous_word == word:
        print('Previous word is equal to current word, updating count')
        previous_count += count
    else:
        print('Previous word not equal to current word')
        if previous_word:
            print(f'{previous_word}\t{previous_count}')
        print(f'Previous word receiving count {count}')
        previous_count = count
        print(f'Previous word receiving word {word}')
        previous_word = word

    print(f'Finishing Iteration {c}')
    c+=1
if previous_word == word:
    print(f'{previous_word}\t{previous_count}')