# Day 16

# Description

import os
import sys


__inputfile__ = 'Day-16-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''.strip()

test2 = '''\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''.strip()

def parse_rule(s: str) -> (str, []):
    name, rest = s.split(': ')
    low, high = rest.split(' or ')
    lmin, lmax = low.split('-')
    hmin, hmax = high.split('-')

    low_range = set(range(int(lmin), int(lmax) + 1))
    high_range = set(range(int(hmin), int(hmax) + 1))

    return (name, low_range.union(high_range))

def parse_input(s: str):
    rules, mine, nearby = s.split('\n\n')

    RULES = {}
    for r in rules.split('\n'):
        name, inclusions = parse_rule(r)
        RULES[name] = inclusions

    mine = list(map(int,mine.split('\n')[1].split(',')))
    others = []
    for n in nearby.split('\n')[1:]:
        others.append(list(map(int, n.split(','))))
    
    return RULES, mine, others

def find_errors(s: str):
    RULES, mine, others = parse_input(s)
    ALLRULES = set().union(*RULES.values())
        
    errors = []

    for other in others:
        for n in other:
            if n not in ALLRULES:
                errors.append(n)

    return sum(errors)

def discard_errors(rules, nearbys):
    ALLRULES = set().union(*rules.values())
        
    good = []

    for other in nearbys:
        for n in other:
            if n not in ALLRULES:
                break
        else: 
            good.append(other)
    
    return good

def determine_fields(s):
    RULES, mine, others = parse_input(s)
    others = discard_errors(RULES,others)
    others_fields = list(map(list, zip(*others))) # Transpose the tickets

    my_ticket = {}
    suitors = []
    for i in range(len(others_fields)):
        field = others_fields[i]
        applicable = set()
        for f, rule in RULES.items():
            if set(field).issubset(rule):
                applicable.add(f)
        suitors.append(applicable)

    while set().union(*suitors) != set():
        for i in range(len(suitors)):
            if len(suitors[i]) == 1:
                field = suitors[i].pop()
                my_ticket[field] = mine[i]
                for s in suitors:
                    s.discard(field)



    return my_ticket

def part2(d):
    result = 1
    for k,v in d.items():
        if k.split(' ')[0] == 'departure':
            result *= v
    return result


if __name__ == "__main__":
    print("Part 1:")
    print(find_errors(input_str))
    print("Part 2:")
    print(part2(determine_fields(input_str)))