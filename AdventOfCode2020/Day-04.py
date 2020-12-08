# Day 04

# Description

import os
import sys
import re
import string

__inputfile__ = 'Day-04-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

# test = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in'''

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def parse():
    ps = input_str.split('\n\n')
   
    passes = [dict(map(lambda s : s.split(":"), re.split("\s", p))) for p in ps]

    return passes

passports = parse()

def is_valid1(exclusions, passport):
    valid_fields = [f for f in FIELDS if f not in exclusions]
    return set(valid_fields).issubset(set(passport.keys()))

def is_valid2(passport):
    def in_range(value, min, max):
        return min <= int(value) and int(value) <= max

    # byr, 4 digits, between 1920 and 2002, inclusive
    # required
    if 'byr' in passport:
        v = passport['byr']
        if not in_range(v, 1920, 2002):
            return False
    else:
        return False

    # iyr, 4 digits, between 2010 and 2020, inclusive
    # required
    if 'iyr' in passport:
        v = passport['iyr']
        if not in_range(v, 2010, 2020):
            return False
    else:
        return False  

    # eyr, 4 digits, between 2020 and 2030, inclusive
    # required
    if 'eyr' in passport:
        v = passport['eyr']
        if not in_range(v, 2020, 2030):
            return False
    else:
        return False 

    # hgt, number followed by 'in' or 'cm'
    # if 'cm', between 150 and 193, inclusive
    # if 'in', between 59 and 76, inclusive
    # required
    if 'hgt' in passport:
        v = passport['hgt']
        num = v[:-2]
        unit = v[-2:]
        if unit == 'cm':
            if not in_range(num, 150, 193):
                return False
        elif unit == 'in':
            if not in_range(num, 59, 76):
                return False
        else: # unit isn't 'cm' or 'in'
            return False
    else:
        return False 

    # hcl, a '#' followed by exactly 6 characters in the hexidecimal set
    # required
    if 'hcl' in passport:
        v = passport['hcl']
        if v[0] != '#' or not all(c in string.hexdigits for c in v[1:]) or len(v) != 7:
            return False
    else:
        return False 

    # ecl, exactly one of amb blu brn gry grn hzl oth
    # required
    if 'ecl' in passport:
        v = passport['ecl']
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not v in colors:
            return False
    else:
        return False

    # pid, 9 digit number, including leading zeros
    # required
    if 'pid' in passport:
        v = passport['pid']
        if len(v) != 9 or not all(c in string.digits for c in v):
            return False
    else:
        return False

    return True

    



if __name__ == "__main__":
    print("Part 1:")
    print(sum(map(lambda x : is_valid1(['cid'], x), passports)))
    print("Part 2:")
    print(sum(map(is_valid2, passports)))
