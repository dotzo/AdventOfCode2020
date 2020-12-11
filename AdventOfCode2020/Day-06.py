# Day 06

# Description

import os
import sys

__inputfile__ = 'Day-06-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
abc

a
b
c

ab
ac

a
a
a
a

b
'''

def parse(str):
    return [s.split() for s in str.split('\n\n')]

def anyone_yes(q):
    return len(set(''.join(q)))

def everyone_yes(qs):
    return len(set.intersection(*map(set, qs)))



if __name__ == "__main__":
    print("Part 1:")
    print(sum(map(anyone_yes, parse(input_str))))

    print("part 2:")
    print(sum(map(everyone_yes, parse(input_str))))