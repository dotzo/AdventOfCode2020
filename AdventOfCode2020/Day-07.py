# Day 07

# Description

import os
import sys
from pprint import pprint

__inputfile__ = 'Day-07-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

# test = '''\
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# '''.strip()

# test = '''\
# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.'''.strip()

def parse_rule(s):
    # {'color': {'color': number}]}
    color, contents = s.split(' bags contain ')
    if ',' in contents:
        contents = contents.split(', ')
    else:
        contents = [contents]

    def parse_contents(t): # '1 bright white bag.' -> ('bright white', 1)
        if t == 'no other bags.':
            return ('none', 0)
        i = t.find(' ') + 1
        num = int(t[:i].strip())
        color = t[i:].strip()
        color = color.replace('.', '')

        if num == 1:
            color = color.replace(' bag', '')
        else:
            color = color.replace(' bags', '')
        return (color, num)

    contents = dict(map(parse_contents, contents))
    return (color, contents)

#RULES = dict(map(parse_rule, test.split('\n')))
RULES = dict(map(parse_rule, input_str.split('\n')))

def can_contain(color, rule): # {'color': number}
    candidates = list(rule.keys())
    if candidates == ['none']:
        return False
    return color in candidates or any([can_contain(color, RULES[r]) for r in candidates])

def count_contents(color):
    if color == 'none':
        return 0
    return sum(RULES[color].values()) + sum([n*count_contents(c) for c,n in RULES[color].items()])



if __name__ == "__main__":
    test_color = 'shiny gold'
    #pprint([(c, can_contain(test_color, rule)) for c, rule in RULES.items()])
    # print("Part 1:")
    # print(sum([can_contain(test_color, rule) for rule in RULES.values()]))

    print("Part 2:")
    print(count_contents(test_color))