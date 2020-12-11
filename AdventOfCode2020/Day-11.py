# Day 11

# Description

import os
import sys
from copy import deepcopy, copy
from pprint import pprint

__inputfile__ = 'Day-11-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

def parse(s):
    return list(map(list, s.split('\n')))

test = '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

test = parse(test)
INPUT = parse(input_str)

def apply_rules(c, NEAR_ONLY=False):
    new = deepcopy(c)
    y_limit = len(new)
    x_limit = len(new[0])
    # rules
    # 1. if L and no adjacent '#', becomes '#'
    # 2. if '#' and four or more adjacent are also '#', then 'L'
    # 3. otherwise, no chage
    # 4. '.' never changes

    def new_value(x,y,space):
        if space == '.':
            return '.'
        nonlocal x_limit, y_limit
        adjacents = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1),(0,-1)]
        if not NEAR_ONLY:
            surroundings = [c[y+dy][x+dx] for dx,dy in adjacents if x+dx in range(x_limit)
                and y+dy in range(y_limit)]
        else:
            surroundings = []
            for dx,dy in adjacents:
                x1 = x+dx
                y1 = y+dy
                while x1 in range(x_limit) and y1 in range(y_limit):
                    vision = c[y1][x1]
                    
                    if vision == '#' or vision == 'L':
                        surroundings.append(vision)
                        break
                    x1 = x1+dx
                    y1 = y1+dy

        
        if space == 'L' and all(map(lambda v: v != '#', surroundings)):
            return '#'

        if space == '#' and sum(map(lambda v: 1 if v == '#' else 0, surroundings)) >= 4 + NEAR_ONLY:
            return 'L'
        return space
    
    for y in range(y_limit):
        for x in range(x_limit):
            new[y][x] = new_value(x,y,c[y][x])
    
    return new

def go_until_stable(c, NEAR_ONLY=False):
    start = deepcopy(c)
    end = apply_rules(start, NEAR_ONLY)
    while start != end:
        start = end
        end = apply_rules(end, NEAR_ONLY)


    return sum([sum(map(lambda v: 1 if v == '#' else 0, row)) for row in end])


if __name__ == "__main__":
    #pprint(list(map(lambda s: ''.join(s), test)))
    #pprint(list(map(lambda s: ''.join(s), apply_rules(test))))

    print("Part 1: ")
    print(go_until_stable(INPUT))
    print("Part 2: ")
    print(go_until_stable(INPUT, NEAR_ONLY = True))
