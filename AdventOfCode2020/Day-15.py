# Day 15

# Description

# import os
# import sys
import time

# __inputfile__ = 'Day-15-input.txt'
# __location__ = os.path.join(sys.path[0], __inputfile__)

# with open(__location__, 'r') as f:
#     input_str = f.read().strip() # Takes the inputfile as a string
input_str = '''17,1,3,16,19,0'''.split(',')
input_str = list(map(int, input_str))

test = [0,3,6]

def play_game(starting_numbers, max_turns):
    memory = {}
    last_said = -1
    turn_number = 1
    toSpeak = -1
    last_seen = -1
    # Seed the memory with the starting numbers
    for v in starting_numbers:
        memory[v] = turn_number
        last_said = v
        turn_number += 1
    
    while turn_number <= max_turns:
        last_seen = memory[last_said]
        # Number has only been said once, never been said before turn_number - 1, say 0
        if last_seen == turn_number - 1:
            toSpeak = 0
        # Number has been sayd before turn_number - 1, say difference of last occurances, remember number
        else:
            toSpeak = turn_number - 1 - last_seen
            memory[last_said] = turn_number - 1
        if toSpeak not in memory:
            memory[toSpeak] = turn_number
        turn_number += 1
        last_said = toSpeak
        #starting_numbers.append(toSpeak)
        #if turn_number % 100000 == 0:
        #    print(turn_number)
    return last_said





if __name__ == "__main__":
    print("Part 1:")
    print(play_game(input_str, 2020))
    print("Part 2:")
    start = time.time()
    print(play_game(input_str, 30000000))
    end = time.time()
    print(end - start)
    