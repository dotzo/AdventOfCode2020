# Day 22

# Description

import os
import sys

__inputfile__ = 'Day-22-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

def parse(s):
    p1, p2 = s.split('\n\n')
    p1, p2 = p1.split('\n')[1:], p2.split('\n')[1:]
    p1_hand = []
    p2_hand = []
    for a,b in zip(p1,p2):
        p1_hand.append(int(a))
        p2_hand.append(int(b))

    return p1_hand, p2_hand


def play(p1,p2,RECURSIVE=False):
    if p1 == []:
        print("Player 2 wins!")
        return p2
    if p2 == []:
        print("Player 1 wins!")
        return p1
    #print("Player 1: ", p1)
    #print("Player 2: ", p2)
    #print()
    if RECURSIVE and len(p1[1:]) >= p1[0] and len(p2[1:]) >= p2[0]:
        winner = sub_game(p1[1:1+p1[0]], p2[1:1+p2[0]], set())
        if winner == 1:
            return play(p1[1:] + p1[:1] + p2[:1], p2[1:], RECURSIVE)
        else:
            return play(p1[1:], p2[1:] + p2[:1] + p1[:1], RECURSIVE)

    if p1[0] > p2[0]:
        return play(p1[1:] + p1[:1] + p2[:1], p2[1:], RECURSIVE)
    else:
        return play(p1[1:], p2[1:] + p2[:1] + p1[:1], RECURSIVE)

def sub_game(p1,p2,seen):
    while True:
        if p1 == []:
            return 2
        hs = ','.join(map(str,p1)) + '\n' + ','.join(map(str,p2))
        if p2 == [] or hs in seen:
            return 1
        #print("Sub-Game Player 1: ", p1)
        #print("Sub-Game PLayer 2: ", p2)
        #print()
        seen.add(hs)

        if len(p1[1:]) >= p1[0] and len(p2[1:]) >= p2[0]:
            winner = sub_game(p1[1:1+p1[0]], p2[1:1+p2[0]], set())
            if winner == 1:
                p1, p2 = p1[1:] + p1[:1] + p2[:1],  p2[1:]
                continue
            else:
                p1, p2 = p1[1:], p2[1:] + p2[:1] + p1[:1]
                continue

        if p1[0] > p2[0]:
            p1, p2 = p1[1:] + p1[:1] + p2[:1],  p2[1:]
        else:
            p1, p2 = p1[1:], p2[1:] + p2[:1] + p1[:1]

def calculate_score(hand):
    return sum([(x+1)*y for x,y in enumerate(reversed(hand))])
    

if __name__ == "__main__":
    hands = parse(input_str)
    #winner_part1 = play(*hands,RECURSIVE=False)
    winner_part2 = play(*hands,RECURSIVE=True)
    print("Part 1:")
    #print(calculate_score(winner_part1))
    print("Part 2: ")
    print(calculate_score(winner_part2))