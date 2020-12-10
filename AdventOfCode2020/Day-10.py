# Day 10

# Description

import os
import sys
from itertools import combinations

__inputfile__ = 'Day-10-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

small_test = '''\
16
10
15
5
1
11
7
19
6
12
4'''

mid_test = '''\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

def parse(s):
    return list(map(int, s.split('\n')))

def find_distribution(joltages):
    joltages.append(max(joltages)+3)
    joltages.append(0)
    joltages.sort()
    
    distro = []

    for i in range(len(joltages) - 1):
        diff = joltages[i+1] - joltages[i]
        distro.append(diff)


    return distro

def partition(n):
    answer = set()
    answer.add((n,))
    for x in range(1, n):
        for y in partition(n - x):
            answer.add((x,) + y)

    return answer

def max_partition(n, cap):
    return len([p for p in partition(n) if max(p) <= cap])

def count_adapters(distribution):
    count = 1
    current_pos = 0
    for i in range(len(distribution)):
        if distribution[i] == 1:
            continue
        # otherwise it's a 3
        # i is now the index of the most recently found 3
        # the difference i - current_pos is the length of the sequence of 1s
        count *= max_partition(i - current_pos, 3)
        current_pos = i+1
    # distrubiton string always ends in a 3
    return count




if __name__ == "__main__":
    test = find_distribution(parse(mid_test))
    print(test)
    # test.append(max(test) + 3)
    # test.append(0)
    # test.sort()
    part1 = find_distribution(parse(input_str))
    print("Part 1:")
    print(len([n for n in part1 if n == 1])*len([n for n in part1 if n == 3]))

    print("Part 2:")
    print(count_adapters(part1))
