# Day X

# Description

input_str = "247819356"
test = "389125467"

import cProfile
import pstats

profile = cProfile.Profile()

def parse(s):
    return list(map(int, s))


def play(cups, rounds):
    for r in range(rounds): 
        current = cups[0]
        reinsert = cups[1:4]
        del cups[1:4]
        destination = current - 1

        while 1:
            if destination < 1:
                destination = 9
            if destination in reinsert:
                destination -= 1
                continue
            else:
                break
        i = cups.index(destination)
        i += 1
        cups[i:i] = reinsert
        c = cups[0]
        cups = cups[1:]
        cups.append(c)
    return cups


def bigPlay(cups, rounds):
    d = {}
    for i in range(1,len(cups)):
        d[cups[i-1]] = cups[i]
    d[cups[-1]] = cups[0]

    d[-1] = cups[0]
    start = -1
    maxLabel = max(cups)

    for i in range(rounds):
        if i % 1000000 == 0: print(i)
        first = d[start]
        x = d[first]
        y = d[x]
        z = d[y]
        firstnext = d[z]
        destination = first - 1

        while 1:
            if destination < 1:
                destination = maxLabel
            if destination in [x,y,z,first]:
                destination -= 1
            else:
                break
        
        d[z] = d[destination]
        d[destination] = x

        d[first] = firstnext
        start = first

    a = d[1]
    b = d[a]
    return a*b
    
def getFromOne(cups):
    i = cups.index(1)
    return ''.join(map(str, cups[i+1:] + cups[:i]))

if __name__ == "__main__":
    input1 = parse(input_str)
    input2 = parse(input_str)
    
    #test = parse(test)
    #print(test)
    #profile.runcall(play, test, 100)
    #ps = pstats.Stats(profile)
    #ps.print_stats()
    #print(test)
    #print(bigPlay(test, 100))

    print("Part 1: ")
    part1 = play(input1, 100)
    print(getFromOne(part1))

    print("Part 2: ")
    input2 = input2 + list(range(10,1000000+1))
    part2 = bigPlay(input2, 10000000)
    print(part2)

