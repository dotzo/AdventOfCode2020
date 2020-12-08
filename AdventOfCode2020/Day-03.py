# Day 03

# From your starting position at the top-left, check the position that is right 3 and down 1. Then, 
# check the position that is right 3 and 
# down 1 from there, and so on until you go past the bottom of the map.

import os
import sys

__inputfile__ = 'Day-03-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read() # Takes the inputfile as a string

test = '''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

def parse(str):
    return str.strip().split()

FIELD = parse(input_str)
#FIELD = parse(test)
WIDTH = len(FIELD[0])
HEIGHT = len(FIELD) 

def toboggan(pos_x, pos_y, rise, run):
    new_x = (pos_x + run) % WIDTH
    new_y = pos_y + rise
    return (new_x, new_y, FIELD[new_y][new_x])

def run_course(pos_x, pos_y, rise, run):
    new_x, new_y = pos_x, pos_y
    trees = 0
    while new_y < HEIGHT - 1:
        new_x, new_y, element = toboggan(new_x, new_y, rise, run)
        # print(new_x, new_y, element)
        if element == '#':
            trees += 1
    return trees
    

    






if __name__ == "__main__":
    R1D1 = run_course(0,0,1,1)
    R3D1 = run_course(0,0,1,3)
    R5D1 = run_course(0,0,1,5)
    R7D1 = run_course(0,0,1,7)
    R1D2 = run_course(0,0,2,1)

    print("R1D1: ", R1D1)
    print("R3D1: ", R3D1)
    print("R5D1: ", R5D1)
    print("R7D1: ", R7D1)
    print("R1D2: ", R1D2)

    print("Product: ", R1D1*R3D1*R5D1*R7D1*R1D2)
