# Day 25

# Description

import os
import sys

__inputfile__ = 'Day-25-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

PRIME = 20201227

def getPrivateKeys(*search, max_iter=16000000):
    v = 1
    loop = 1
    while search and loop < max_iter:
        v = (v*7) % PRIME
        if v in search:
            yield (v, loop)
        loop += 1
        #if loop % 100000 == 0:
            #print(loop)



if __name__ == "__main__":
    card, door = tuple(map(int, input_str.split('\n')))
    print(card, door)
    keys = dict(getPrivateKeys(card, door))
    print("Part 1:")
    print(keys)
    print(
        pow(card, keys[door], PRIME),
        pow(door, keys[card], PRIME)
    )