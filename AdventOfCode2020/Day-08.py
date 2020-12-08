# Day 08

# Handheld game console instrucitons assembly

import os
import sys
from pprint import pprint

__inputfile__ = 'Day-08-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.strip()

def parse_instruction(s):
    opcode, number = s.split(' ')
    return (opcode, int(number))


def run_code(instructions):
    already_run = []
    acc = 0
    cycle = 0
    def run_opcode(opcode, number):
        nonlocal cycle
        nonlocal acc
        if opcode == 'nop':
            cycle += 1
        elif opcode == 'jmp':
            cycle = cycle + number
        elif opcode == 'acc':
            cycle += 1
            acc += number
        return
    
    while True:
        if cycle == len(instructions):
            return (True, acc)
        elif cycle in already_run or cycle < 0 or cycle > len(instructions):
            return (False, acc)
        
        already_run.append(cycle)
        run_opcode(*instructions[cycle])

def uncorrupt(instructions):
    for i in range(len(instructions)):
        copy = instructions.copy()
        opcode, num = copy[i]
        if opcode == 'acc':
            continue
        elif opcode == 'jmp':
            copy[i] = ('nop', num)
        elif opcode == 'nop':
            copy[i] = ('jmp', num)
        isTerminate, accumulator = run_code(copy)
        if isTerminate:
            return accumulator
        
            

if __name__ == "__main__":
    program = list(map(parse_instruction, input_str.split('\n')))
    test_program = list(map(parse_instruction, test.split('\n')))
    print("\nPart 1:")
    print(run_code(program)[1])
    print("\nPart 2:")
    print(uncorrupt(program))