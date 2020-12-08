# Day 02

# To try to debug the problem, they have created a list (your puzzle input) of passwords 
# (according to the corrupted database) and the corporate policy when that password was set.

# For example, suppose you have the following list:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and 
# highest number of times a given letter must appear for the password to be valid. 
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

import os
import sys

__inputfile__ = 'Day-02-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

entries = input_str.split('\n')
entries = list(map(lambda s: s.split(': '), entries))

# Part 1 Function
def good_pass(rulepass):
    rules = rulepass[0].split(' ')
    letter = rules[1]
    minmax = list(map(int, rules[0].split('-')))
    password = rulepass[1]
    # print(rules, letter, minmax, password)
    return len([c for c in password if c == letter]) in range(minmax[0], minmax[1]+1)

def good_pass_2(rulepass):
    rules = rulepass[0].split(' ')
    letter = rules[1]
    minmax = list(map(int, rules[0].split('-')))
    password = rulepass[1]

    return (password[minmax[0]-1] == letter) ^ (password[minmax[1]-1] == letter)


if __name__ == "__main__":
    # Part 1
    print(sum(map(good_pass, entries)))

    # Part 2
    print(sum(map(good_pass_2, entries)))