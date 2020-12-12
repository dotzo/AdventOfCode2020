# Day 12

# Description

import os
import sys

__inputfile__ = 'Day-12-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
F10
N3
F7
R90
F11'''.strip()

def parse(s: [str]) -> [(str,int)]:
    return [(line[0], int(line[1:])) for line in s.split("\n")]

def sail(instructions: [(str,int)]) -> int:
    x, y = 0, 0
    # first element will be the current heading
    dirs = ['E', 'S', 'W', 'N']

    for i,d in instructions:
        #print("Step: " + str(i) + ',' + str(d))
        # Take care of turning
        if i == 'R':
            turn = d//90
            dirs = dirs[turn:] + dirs[:turn]
        elif i == 'L':
            turn = (-1)*d//90
            dirs = dirs[turn:] + dirs[:turn]

        if i == 'F':
            i = dirs[0]

        if i == 'N':
            y += d
        elif i == 'S':
            y -= d
        elif i == 'E':
            #print('east')
            x += d
        elif i == 'W':
            x -= d
        #print("Resulting position: " + str(x) + "," + str(y))
    return abs(x) + abs(y)

def sail_to_waypoint(instructions: [(str,int)]) -> int:
    # Ship's Coordinates
    x, y = 0, 0

    # Waypoint's offset
    dx, dy = 10,1

    for i,t in instructions:
        #print("Instruction: " + str(i) + str(t))
        # Move toward the waypoint
        if i == 'F':
            x += t*dx
            y += t*dy
        # Move waypoint itself
        elif i == 'N':
            dy += t
        elif i == 'S':
            dy -= t
        elif i == 'E':
            dx += t
        elif i == 'W':
            dx -= t
        # Rotate waypoint about the ship
        else:
            theta = (t//90) % 4
            if i == 'L':
                theta = -theta
            # R90 or L270
            if theta in [1, -3]:
                dx,dy = dy,-dx
            elif theta in [2, -2]:
                dx,dy = -dx,-dy
            elif theta in [3, -1]:
                dx,dy = -dy,dx
        #print("Resultant: " + str(x) + ',' + str(y))
    return abs(x) + abs(y)



if __name__ == "__main__":
    test = parse(test)
    INPUT = parse(input_str)
    print("Part 1: ")
    print(sail(INPUT))
    print("Part 2: ")
    print(sail_to_waypoint(INPUT))