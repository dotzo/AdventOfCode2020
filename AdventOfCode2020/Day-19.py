# Day 19

# Description

import os
import sys
import re
from pprint import pprint

__inputfile__ = 'Day-19-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
0: 3 | 1 5
1: 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''


def create_cell(first, second):
    res = set()
    if first == set() or second == set():
        return set()
    for f in first:
        for s in second:
            res.add((f,s))
    return res


def read_grammar(grammar):
    rules = grammar.split("\n")
    v_rules = []
    t_rules = []

    for rule in rules:
        left, right = rule.split(": ")

        # for two or more results from a variable
        right = right[0:].split(" | ")
        for ri in right:

            # it is a terminal
            if '\"' == ri[0]:
                t_rules.append([left, tuple(ri[1])])

            # it is a variable
            else:
                v_rules.append([left, tuple(ri.split(' '))])
    return v_rules, t_rules


def cyk_alg(varies, terms, inp):
    length = len(inp)
    var0 = [va[0] for va in varies]
    var1 = [va[1] for va in varies]

    # table on which we run the algorithm
    table = [[set() for _ in range(length-i)] for i in range(length)]

    # Deal with variables
    for i in range(length):
        for te in terms:
            if inp[i] == te[1][0]:
                table[0][i].add(te[0])

    # Deal with terminals
    # its complexity is O(|G|*n^3)
    for i in range(1, length):
        for j in range(length - i):
            for k in range(i):
                row = create_cell(table[k][j], table[i-k-1][j+k+1])
                for ro in row:
                    if ro in var1:
                        table[i][j].add(var0[var1.index(ro)])

    # if the last element of table contains "S" the input belongs to the grammar
    return table


def show_result(tab, inp):
    for c in inp:
        print("\t{}".format(c), end="\t")
    print()
    for i in range(len(inp)):
        print(i+1, end="")
        for c in tab[i]:
            if c == set():
                print("\t{}".format("_"), end="\t")
            else:
                print("\t{}".format(c), end="\t")
        print()

    if '0' in tab[len(inp)-1][0]:
        print("The input belongs to this context free grammar!")
    else:
        print("The input does not belong to this context free grammar!")

def in_language(g, w):
    return '0' in cyk_alg(*read_grammar(g), w)[len(w)-1][0]


if __name__ == "__main__":
    input = test.split('\n\n')
    rules, tests = input[0], input[1].split('\n')
    print("Part 1:")
    v, t = read_grammar(rules)
    pprint(v)
    pprint(t)
    show_result(cyk_alg(v, t, 'abb'), 'abb')
    print(in_language(rules, 'ab'))
    #print(sum(map(lambda x: in_language(rules, x), tests)))
    
    


