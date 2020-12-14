# Day 14

# Description

import os
import sys
from itertools import chain, combinations

def powerset(iterable):
    #"powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

__inputfile__ = 'Day-14-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip().split('\n') # Takes the inputfile as a string

test = '''\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''.strip().split('\n')

test2 = '''\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.strip().split('\n')

def parse_mem(mem: str) -> (int, int):
    # "mem[8] = 11"
    mem = mem.replace("mem[", "")
    mem = mem.replace("] = ", ",")
    mem = mem.split(",")
    return int(mem[0]), int(mem[1])    

## Part 1 Functions
def parse_mask(mask: str) -> (int, int):
    mask = mask[-36:]
    ones_mask = 0
    zeros_mask = 0
    for i,v in enumerate(reversed(mask)):
        #print(i,v)
        if v == 'X':
            continue
        elif v == '1':
            ones_mask += 1 << i
        elif v == '0':
            zeros_mask += 1 << i

    return (ones_mask, zeros_mask)

def apply_mask(ones, zeros, value):
    value |= ones
    value &= ~zeros
    return value

def process_input(input: [str]) -> int:
    memory = {}
    for line in input:
        if line[:2] == 'ma':
            ones, zeros = parse_mask(line)
        else:
            pos, val = parse_mem(line)
            memory[pos] = apply_mask(ones, zeros, val)
    return sum(memory.values())
    

## Part 2 Functions    
def parse_mask2(mask: str) -> (int, int, [int]):
    mask = mask[-36:]
    ones_mask = 0
    x_mask = 0
    x_pos = []
    for i,v in enumerate(reversed(mask)):
        if v == 'X':
            x_pos.append(i)
            x_mask += 1 << i
        elif v == '1':
            ones_mask += 1 << i
    return ones_mask, x_mask, x_pos

def apply_mask2(ones, x_mask, x_pos, pos) -> [int]:
    pos |= ones
    pos &= ~x_mask
    ret = []
    for xs in powerset(x_pos):
        ret.append(pos+sum(map(lambda i: 1<<i, xs)))
    return ret
        
def process_input2(input: [str]) -> int:
    memory = {}
    ones = 0
    x_mask = 0
    xs = []
    for line in input:
        if line[:2] == 'ma':
            ones, x_mask, xs = parse_mask2(line)
        else:
            pos, val = parse_mem(line)
            for p in apply_mask2(ones, x_mask, xs, pos):
                memory[p] = val
    return sum(memory.values())


if __name__ == "__main__":
    print("Part 1: ")
    print(process_input(input_str))
    print("Part 2: ")
    print(process_input2(input_str))