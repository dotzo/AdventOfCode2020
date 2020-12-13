# Day 13

# Description

import os
import sys

__inputfile__ = 'Day-13-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
939
7,13,x,x,59,x,31,19'''.strip()

def parse(s: str) -> (int, [int]):
    t = s.split('\n')
    t[1] = [int(v) for v in t[1].split(',') if v != 'x']
    return (int(t[0]), t[1])

def find_bus(goal: int, busses: [int]) -> (int, int):
    # wait_time = goal - (goal + n - (goal % n)) = n - goal % n
    wait_times = [b - goal % b for b in busses]
    wait_bus = sorted(list(zip(wait_times, busses)))
    return wait_bus[0]

# Implement the Extended Euclidean Algorithm
def gcdExtended(a,b):
    if a == 0:
        return b,0,1
    
    gcd,x1,y1 = gcdExtended(b%a,a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd,x,y

def buildSystem(busses: [str]) -> [(int,int)]:
    return [((int(b) - i) % int(b), int(b)) for i,b in enumerate(busses) if b != 'x']


def chineseRemainderTheorem(system: [(int,int)]) -> int:
    if len(system) == 1:
        return system[0][0]
    
    a1, n1 = system.pop()
    a2, n2 = system.pop()

    g, m1, m2 = gcdExtended(n1, n2)
    x = (a1*m2*n2 + a2*m1*n1) % (n1*n2)

    system.append((x, n1*n2))

    return chineseRemainderTheorem(system)

if __name__ == "__main__":
    part1 = find_bus(*parse(input_str))
    part2 = input_str.split('\n')[1].split(',')
    part2 = buildSystem(part2)
    print("Part 1: ")
    print(part1[0]*part1[1])
    print("Part 2: ")
    print(chineseRemainderTheorem(part2))