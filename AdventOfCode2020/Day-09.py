# Day 09

# Description

import os
import sys

__inputfile__ = 'Day-09-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

WINDOW = 25

def parse(s):
    return list(map(int, s.split('\n')))

def pair_sums(nums):
    result = set()
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            result.add(nums[i] + nums[j])

    return result

def find_wrong(numbers):
    for i in range(len(numbers[WINDOW:])):
        tester = numbers[WINDOW+i]
        test_range = numbers[i: i+WINDOW]
        if tester not in pair_sums(test_range):
            return tester


def contiguous_sum(numbers, goal):
    for size in range(2, len(numbers) - 1):
        for i in range(len(numbers) - size):
            testRange = numbers[i:i+size]
            if sum(testRange) == goal:
                return min(testRange) + max(testRange)

if __name__ == "__main__":
    testing = parse(test)
    INPUT = parse(input_str)
    part1 = find_wrong(INPUT)
    part2 = contiguous_sum(INPUT, part1)
    print("Part 1:")
    print(part1)
    print("Part 2:")
    print(part2)
    