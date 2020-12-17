# Day 17

# Description

import os
import sys
from pprint import pprint

__inputfile__ = 'Day-17-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
.#.
..#
###'''

def build_initial(s):
    t = s.split('\n')
    space = {}
    for y in range(len(t)):
        for x in range(len(t[0])):
            space[(x,y,0)] = t[y][x]
    return space

def max_dim(space):
    mx, my, mz = 0, 0 ,0
    for (x,y,z), v in space.items():
        if v == '.':
            continue
        if x > mx:
            mx = x
        if y > my:
            my = y
        if z > mz:
            mz = z
        
    return mx, my, mz

def min_dim(space):
    mx, my, mz = 0, 0 ,0
    for (x,y,z),v in space.items():
        if v == '.':
            continue
        if x < mx:
            mx = x
        if y < my:
            my = y
        if z < mz:
            mz = z
        
    return mx, my, mz

def build_empty_space(minx,miny,minz,maxx,maxy,maxz):
    space = {}
    for x in range(minx,maxx+1):
        for y in range(miny,maxy+1):
            for z in range(minz,maxz+1):
                space[(x,y,z)] = '.'
    return space

def seed_space(canvas, paint):
    for k,v in paint.items():
        canvas[k] = v

def update_space(space):
    minx, miny, minz = min_dim(space)
    maxx, maxy, maxz = max_dim(space)
    check_space = build_empty_space(minx-1,miny-1,minz-1,maxx+1,maxy+1,maxz+1)
    update_space = build_empty_space(minx-1,miny-1,minz-1,maxx+1,maxy+1,maxz+1)
    
    seed_space(check_space, space)







    return update_space




if __name__ == "__main__":
    space = build_initial(test)
    #pprint(update_space(space))
