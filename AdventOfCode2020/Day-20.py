# Day X

# Description

import os
import sys
from pprint import pprint
import math

__inputfile__ = 'Day-20-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

class Tile:
    def __init__(self, s: str):
        rows = s.split('\n')
        id_line = rows[0]
        piece = rows[1:]
        self.grid = piece
        self.id = int(id_line.split(' ')[1][:-1])

        top = piece[0]
        bottom = piece[-1]
        left, right = [], []
        for r in piece:
            left.append(r[0])
            right.append(r[-1])

        self.edges = {'top': top, 'lft': ''.join(left), 'rgt': ''.join(right), 'bot': bottom}

    ## Define the symmetries ##
    # Identity symmetry
    def r0(self):
        e = self.edges
        return {'top': e['top'], 'lft': e['lft'], 'rgt': e['rgt'], 'bot': e['bot']}
    
    # 90 degree rotation ccw
    def r1(self):
        e = self.edges
        return {'top': e['rgt'], 'lft': e['top'][::-1], 'rgt': e['bot'][::-1], 'bot': e['lft']}
    
    # 180 degree rotation ccw
    def r2(self):
        e = self.edges
        return {'top': e['bot'][::-1], 'lft': e['rgt'][::-1], 'rgt': e['lft'][::-1], 'bot': e['top'][::-1]}
    
    # 278 degree rotation ccw
    def r3(self):
        e = self.edges
        return {'top': e['lft'][::-1], 'lft': e['bot'], 'rgt': e['top'], 'bot': e['rgt'][::-1]}
    
    # Flip across horizontal
    def h(self):
        e = self.edges
        return {'top': e['bot'], 'lft': e['lft'][::-1], 'rgt': e['rgt'][::-1], 'bot': e['top']}
    
    # Flip across vertical
    def v(self):
        e = self.edges
        return {'top': e['top'][::-1], 'lft': e['rgt'], 'rgt': e['lft'], 'bot': e['bot'][::-1]}
    
    # Flip across main diagonal
    def fmain(self):
        e = self.edges
        return {'top': e['lft'], 'lft': e['top'], 'rgt': e['bot'], 'bot': e['rgt']}
    
    # Flip across minor diagonal
    def fminor(self):
        e = self.edges
        return {'top': e['rgt'][::-1], 'lft': e['bot'][::-1], 'rgt': e['top'][::-1], 'bot': e['lft'][::-1]}
    

    def getSymmetries(self):
        return [self.r0(), self.r1(), self.r2(), self.r3(), self.h(), self.v(), self.fmain(), self.fminor()]
    
    def orientByNumber(self, n):
        if n == 0:
            return self.r0()
        elif n == 1: 
            return self.r1()
        elif n == 2:
            return self.r2()
        elif n == 3:
            return self.r3()
        elif n == 4:
            return self.h()
        elif n == 5:
            return self.v()
        elif n == 6:
            return self.fmain()
        elif n== 7:
            return self.fminor()
    
def getGrid(grid, orientation=0):
    g = grid
    if orientation == 0: #id
        return g
    elif orientation == 1: # 90 ccw
        return [list(x) for x in zip(*g)][::-1]
    elif orientation == 2: # 180
        return [r[::-1] for r in g][::-1]
    elif orientation == 3: # 270 ccw
        t = g[::-1]
        return [list(x) for x in zip(*t)]
    elif orientation == 4: # flip about horizontal
        return g[::-1]
    elif orientation == 5: # flip about vertical
        return [r[::-1] for r in g]
    elif orientation == 6: # transpose
        return [list(x) for x in zip(*g)]
    elif orientation == 7: # transpose along other diagonal
        t = [r[::-1] for r in g][::-1]
        return [list(x) for x in zip(*t)]

def gen_tiling(tiles):
    dim = math.isqrt(len(tiles))
    def impl(tiling, x, y, seen):
        if y == dim:
            return tiling
        next_x = x+1
        next_y = y
        if next_x == dim:
            next_x = 0
            next_y += 1
        for tile in tiles:
            if tile.id in seen:
                continue
            seen.add(tile.id)
            tSyms = tile.getSymmetries()
            for i in range(len(tSyms)):
                top = tSyms[i]['top']
                left = tSyms[i]['lft']

                if x > 0:
                    neighbor, neighbor_orient = tiling[x-1][y]
                    neighbor_right = neighbor.orientByNumber(neighbor_orient)['rgt']
                    if neighbor_right != left:
                        continue
                
                if y > 0:
                    neighbor, neighbor_orient = tiling[x][y-1]
                    neighbor_bottom = neighbor.orientByNumber(neighbor_orient)['bot']
                    if neighbor_bottom != top:
                        continue
                tiling[x][y] = (tile, i)
                answer = impl(tiling, next_x, next_y, seen)
                if answer is not None:
                    return answer
            seen.remove(tile.id)
        tiling[x][y] = None
        return None
    tiling = [[None]*dim for _ in range(dim)]
    return impl(tiling, 0, 0, set())

def part1(tiles):
    tiling = gen_tiling(tiles)
    corners = [tiling[0][0], tiling[0][-1], tiling[-1][0], tiling[-1][-1]]
    answer = 1
    for t,_ in corners:
        answer *= t.id
    print("Part 1: ")   
    print(answer)

def make_superimage(tiling):
    output = []
    for row in tiling:
        grids = []
        for tile, orient in row:
            grid = getGrid(tile.grid, orient)
            # get rid of the borders
            grid = [l[1:-1] for l in grid[1:-1]]
            grids.append(grid)
        
        for y in range(len(grids[0][0])):
            out_row = []
            for idx in range(len(grids)):
                out_row.extend(grids[idx][x][y] for x in range(len(grids[idx])))
            output.append(''.join(out_row))
    return output

MONSTER_PATTERN = '''\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


def test_for_monsters(image):
    monster_coords = []
    max_x = 0
    max_y = 0
    for dy, line in enumerate(MONSTER_PATTERN.splitlines()):
        for dx, c in enumerate(line):
            if c == '#':
                monster_coords.append((dx,dy))
                max_x = max(dx, max_x)
                max_y = max(dy, max_y)
    monster_tiles = set()
    for y in range(len(image)):
        if y+max_y >= len(image):
            break
        for x in range(len(image[y])):
            if max_x+x >= len(image[y]):
                break
            has_monster = True
            for dx,dy in monster_coords:
                if image[y+dy][x+dx] != '#':
                    has_monster = False
                    break
            if has_monster:
                for dx, dy in monster_coords:
                    monster_tiles.add((x+dx, y+dy))
    if len(monster_tiles) == 0:
        return None
    all_pounds = set()
    for y, row in enumerate(image):
        for x, c in enumerate(row):
            if c == '#':
                all_pounds.add((x,y))

    return len(all_pounds - monster_tiles)


def part2(tiles):
    tiling = gen_tiling(tiles)
    image = make_superimage(tiling)
    for i in range(8):
        answer = test_for_monsters([''.join(l) for l in getGrid(image, i)])
        if answer is not None:
            break

    print("Part 2:")
    print(answer)

if __name__ == "__main__":
    str_tiles = input_str.split('\n\n')
    tiles = []
    for s in str_tiles:
        tiles.append(Tile(s))
    part1(tiles)
    part2(tiles)
