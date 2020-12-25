'''
Day:            25
File:           combo_breaker.py
Author:         Rishabh Ranjan
Last Modified:  12/25/2020
'''

import math

def transform(value, subject_number):
    return (value * subject_number) % 20201227

def main():
    f = open('day_25_input.txt', 'r')
    public_keys = list(map(int, f.read().splitlines()))
    f.close()
    subject_number = 7
    value = 1
    loop_sizes = []
    i = 1
    while len(loop_sizes) < 2:
        value = transform(value, subject_number)
        if value == public_keys[0]:
            loop_sizes.insert(0, i)
        if value == public_keys[1]:
            loop_sizes.append(i)
        i += 1
    value = 1
    subject_number = public_keys[1]
    for i in range(loop_sizes[0]):
        value = transform(value, subject_number)
    print("Part 1 Answer: ", value)

if __name__ == '__main__':
    main()
