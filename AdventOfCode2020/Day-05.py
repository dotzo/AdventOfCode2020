# Day 05

# Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, 
# where F means "front", B means "back", L means "left", and R means "right".

# Every seat also has a unique seat ID: multiply the row by 8, then add the column. 
# In this example, the seat has ID 44 * 8 + 5 = 357.

import os
import sys

__inputfile__ = 'Day-05-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

#test = 'BFFFBBFRRR'
seats = input_str.split()
def convert(BSP):
    str = BSP.replace('F', '0')
    str = str.replace('B', '1')
    str = str.replace('R', '1')
    str = str.replace('L', '0')

    return (int(str[0:7], 2), int(str[7:], 2))

def hash(row, col):
    return row * 8 + col

def find_missing(l):
    seatIDs = l
    seatIDs.sort()

    for i in range(len(seatIDs) - 1):
        if seatIDs[i+1] - seatIDs[i] == 2:
            return seatIDs[i] + 1 


if __name__ == "__main__":
    seatIDs = [hash(*convert(seat)) for seat in seats]
    print("Part 1:")
    print(max(seatIDs))

    print("Part 2:")
    print(find_missing(seatIDs))