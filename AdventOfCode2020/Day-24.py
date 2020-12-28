# Day 24

# Hex Tiles

import os
import sys

__inputfile__ = 'Day-24-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''.strip().split('\n')

# using axial coordinates, q = flat, r = \
def getTile(instructions, q, r):
    while instructions:
        i = instructions[0]
        j = None

        # q row
        if i == 'w':
            q -= 1
            j = None
        elif i == 'e':
            q += 1
            j = None
        elif i == 'n':
            j = instructions[1]
            r += 1
            q += 0 if j == 'w' else 1
        elif i == 's':
            j = instructions[1]
            r -= 1
            q -= 0 if j == 'e' else 1

        instructions = instructions[2:] if j else instructions[1:]

    return (q, r)

def getBlackTiles(inst_set):
    black_tiles = set()
    coords = None
    for inst in inst_set:
        coords = getTile(inst, 0,0)
        if coords in black_tiles:
            black_tiles.remove(coords)
        else:
            black_tiles.add(coords)

    return black_tiles

    
def flipByDay(inst_set, days):
    initBlacks = getBlackTiles(inst_set)
    #print(initBlacks)
    #print(len(initBlacks))
    qs, rs = list(zip(*initBlacks))
    max_q = max(qs)
    min_q = min(qs)
    max_r = max(rs)
    min_r = min(rs)

    # build_initial
    currSpace = build_empty_space(min_q, max_q, min_r, max_r)
    for hex in initBlacks:
        currSpace[hex] = 'black'
    #print(currSpace)
    for _ in range(days):
        currSpace = update_space(currSpace)
    #print()
    return currSpace

def countBlackTiles(space):
    count = 0
    for v in space.values():
        if v == 'black':
            count += 1
    return count

def build_empty_space(minq,maxq,minr,maxr):
    space = {}
    for q in range(minq,maxq+1):
        for r in range(minr,maxr+1):
            #print(q,r)
            space[(q,r)] = 'white'
    
    return space

def seed_space(canvas, paint):
    for k,v in paint.items():
        canvas[k] = v

def check_adjacents(space, q,r):
    active = 0
    adjacents = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]
    for dq,dr in adjacents:
        if (q+dq,r+dr) not in space:
            continue
        if space[(q+dq, r+dr)] == 'black':
            active += 1

    return active

def update_space(space):
    minq, minr = min_dim(space)
    maxq, maxr = max_dim(space)
    check_space = build_empty_space(minq-1, maxq + 1, minr - 1, maxr + 1)
    update_space = build_empty_space(minq-1, maxq + 1, minr - 1, maxr + 1)
    
    seed_space(check_space, space)
    seed_space(update_space, space)
    #print("check_space")
    #print(check_space)
    for k,v in check_space.items():
        active_neighbors = check_adjacents(check_space, *k)
        if check_space[k] == 'black' and (active_neighbors == 0 or active_neighbors > 2):
            update_space[k] = 'white'
        elif check_space[k] == 'white' and active_neighbors == 2:
            update_space[k] = 'black'
        else:
            continue
    return update_space

def max_dim(space):
    mx, my = 0, 0
    for (x,y), v in space.items():
        if v == 'white':
            continue
        if x > mx:
            mx = x
        if y > my:
            my = y

        
    return mx, my

def min_dim(space):
    mx, my = 0, 0
    for (x,y), v in space.items():
        if v == 'white':
            continue
        if x < mx:
            mx = x
        if y < my:
            my = y
        
    return mx, my



if __name__ == "__main__":
    input = input_str.split('\n')
    print("Part 1:")
    print(len(getBlackTiles(input)))

    print("Part 2:")
    print(countBlackTiles(flipByDay(input, 100)))