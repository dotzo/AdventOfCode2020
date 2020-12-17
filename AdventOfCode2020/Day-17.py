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

# Part 1: 3D
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

def check_adjacents(space, x,y,z):
    active = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            for dz in [-1,0,1]:
                if (dx,dy,dz) == (0,0,0):
                    continue
                if (x+dx,y+dy,z+dz) not in space:
                    continue
                if space[(x+dx,y+dy,z+dz)] == '#':
                    active += 1
    return active

def update_space(space):
    minx, miny, minz = min_dim(space)
    maxx, maxy, maxz = max_dim(space)
    check_space = build_empty_space(minx-1,miny-1,minz-1,maxx+1,maxy+1,maxz+1)
    update_space = build_empty_space(minx-1,miny-1,minz-1,maxx+1,maxy+1,maxz+1)
    
    seed_space(check_space, space)

    for k,v in check_space.items():
        active_neighbors = check_adjacents(check_space, *k)
        if check_space[k] == '.' and active_neighbors == 3:
            update_space[k] = '#'
        elif check_space[k] == '#' and active_neighbors in [2,3]:
            update_space[k] = '#'
        else:
            # update_space[k] = '.'
            continue
    return update_space

def count_actives(space):
    return len(list(filter(lambda x: x == '#', space.values())))

# Part 2 - 4D
def build_initial_4D(s):
    t = s.split('\n')
    space = {}
    for y in range(len(t)):
        for x in range(len(t[0])):
            space[(x,y,0,0)] = t[y][x]
    return space

def max_dim_4D(space):
    mx, my, mz, mw = 0, 0, 0, 0
    for (x,y,z,w), v in space.items():
        if v == '.':
            continue
        if x > mx:
            mx = x
        if y > my:
            my = y
        if z > mz:
            mz = z
        if w > mw:
            mw = w
        
    return mx, my, mz, mw

def min_dim_4D(space):
    mx, my, mz, mw = 0, 0, 0, 0
    for (x,y,z,w), v in space.items():
        if v == '.':
            continue
        if x < mx:
            mx = x
        if y < my:
            my = y
        if z < mz:
            mz = z
        if w < mw:
            mw = w
        
    return mx, my, mz, mw

def build_empty_space_4D(minx,miny,minz,minw, maxx,maxy,maxz,maxw):
    space = {}
    for x in range(minx,maxx+1):
        for y in range(miny,maxy+1):
            for z in range(minz,maxz+1):
                for w in range(minw,maxw+1):
                    space[(x,y,z,w)] = '.'
    return space

def check_adjacents_4D(space, x,y,z,w):
    active = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            for dz in [-1,0,1]:
                for dw in [-1,0,1]:
                    if (dx,dy,dz,dw) == (0,0,0,0):
                        continue
                    if (x+dx,y+dy,z+dz,w+dw) not in space:
                        continue
                    if space[(x+dx,y+dy,z+dz,w+dw)] == '#':
                        active += 1
    return active

def update_space_4D(space):
    minx, miny, minz, minw = min_dim_4D(space)
    maxx, maxy, maxz, maxw = max_dim_4D(space)
    check_space = build_empty_space_4D(minx-1,miny-1,minz-1,minw-1,maxx+1,maxy+1,maxz+1,maxw+1)
    update_space = build_empty_space_4D(minx-1,miny-1,minz-1,minw-1,maxx+1,maxy+1,maxz+1,maxw+1)
    
    seed_space(check_space, space)

    for k,v in check_space.items():
        active_neighbors = check_adjacents_4D(check_space, *k)
        if check_space[k] == '.' and active_neighbors == 3:
            update_space[k] = '#'
        elif check_space[k] == '#' and active_neighbors in [2,3]:
            update_space[k] = '#'
        else:
            # update_space[k] = '.'
            continue
    return update_space





if __name__ == "__main__":
    space_3D = build_initial(input_str)
    space_4D = build_initial_4D(input_str)
    for _ in range(6):
        space_3D = update_space(space_3D)
        space_4D = update_space_4D(space_4D)
    

    print("Part 1:")
    print(count_actives(space_3D))
    print("Part 2:")
    print(count_actives(space_4D))
