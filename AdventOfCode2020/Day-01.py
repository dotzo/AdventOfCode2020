# Day 1

# Before you leave, the Elves in accounting just need you to fix your expense report 
# (your puzzle input); apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and then 
# multiply those two numbers together.

import os
import sys

__inputfile__ = 'Day-01-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    inputlist = f.read().split()

inputlist = list(map(int, inputlist))
inputlist.sort()

def pairsum(target, list):
    for i in range(len(list)):
        for j in reversed(range(len(list))):
            a = list[i]
            b = list[j]
            if a + b < 2020:
                continue
            if a + b == 2020:
                return (a, b, a*b)

def tripletsum(target, list):
    for i in range(len(list)):
        for k in range(i, len(list)):
            for j in reversed(range(len(list))):
                a = list[i]
                b = list[j]
                c = list[k]
                if a + b + c == 2020:
                    return (a, b, c,  a*b*c)

print(pairsum(2020, inputlist))
print(tripletsum(2020, inputlist))