# Day X

# Description

import os
import sys
from collections import Counter
from pprint import pprint

__inputfile__ = 'Day-21-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''

def parse(s):
    ret = []
    for food in s.split('\n'):
        ing, ale = food.split(' (contains ')
        ing = set(ing.split(' '))
        ale = ale[:-1].split(', ')
        ret.append((ing,ale))
    return ret

def match_allergens(foods):
    allergens = {}
    all_ings = Counter()
    for food in foods:
        ings, ales = food
        for a in ales:
            #print(a)
            if a not in allergens:
                allergens[a] = ings
            else:
                allergens[a] = allergens[a].intersection(ings)
        all_ings.update(ings)
    pprint(allergens)

    return allergens, all_ings


def part1(allergens, all_ings):
    for a in allergens:
        for w in allergens[a]:
            all_ings.pop(w) if w in all_ings else None
    
    return sum(all_ings.values())

def part2(allergens):
    ings_with_all = {}

    while allergens:
        for a, i in allergens.items():
            if len(i) == 1:
                ings_with_all[a] = i
                del allergens[a]
                break
        seen = set().union(*ings_with_all.values())
        for a in allergens:
            allergens[a] -= seen
    

    return ','.join(list(k)[0] for k in list(zip(*sorted(ings_with_all.items())))[1])




if __name__ == "__main__":
    inp = parse(input_str)
    alls, count_ings = match_allergens(inp)
    print("Part 1:")
    pprint(part1(alls, count_ings))
    print("Part 2:")
    print(part2(alls))
    
