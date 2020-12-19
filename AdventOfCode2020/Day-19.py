# Day 19

# Below solution taken from reddit user r/ai_prof
# I spent a long time banging my head against the CYK wall
# and then found this super elegant solution that I SHOULD have thought of
# a long time ago.  Thank you to them.  Definitely hardest day by far.

# r/ai_prof original sourcecode: https://nopaste.ml/?l=py#XQAAAQDoAwAAAAAAAAARiAlnWkYw4z9Mqogy9BnsTxKRx5ZimKog89D0yCAx/5vFt/Ladi4EYJ63HubkbBNqnrfK/jwD0fO6c/PEhrsej4nK+WeCFbuelRIDfPYGuD99YoDQCwll+w75xUDSVJ60UgA/6ObW4IULLIn6NmVcOAGy/dewu9Uo4W0TUtGGxICsMvLWwX4DYJmrhPj9gOR2FfPw97eZxDVX0n5mM7Zol1AwYwAUNWK1//ovqlwlWIzNs6gQCsuL/WMt8qCBStXo907ZtS2pxbZkPUMgkv7VMMzu/KPkkMASWuYdbtyIEocy4VcEV5dnIdHlhDzPsabgLuWHALR0Kp089TgaMGWiZVufnp4ZNIAFb4e7tR5xE7tr6mEHdujxq8Vc2MRv8xjCkdhGifFx2YWnkHb4qy0uzVZi9Uk6BrFISrJG0whMMXCFgizkTB2ff4IV6pOlj2v6hvNQlxilpp8fSAvwwEDy4cotYIJ6b4jqTv0FER7C8cEPZAgPgEeBOMX76a1qndb0h0MeqXDD/Ve267tqnS1FbSFkuLoNtuI5fxmi/HmQcAcX7X5I2hSv/v6dHDcJGR8H8DDMP4belU5ZHAReRWXU7PvtP/AzYAYmgQFzIpLPeyd0Nn7Hp/B54Vr18ySRnIamdrp+Q8UnOvRZ5165yQ2BqyRZ/7WfMLw=
# link to reddit post: https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/ggdxmpa/
import os
import sys
from pprint import pprint

__inputfile__ = 'Day-19-input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''

# recursively identify if the string s can be built using the sequence of rules given
def can_be_built(s: str, seq: [int]) -> bool:
    if s == '' or seq == []: # we ran out of stuff to check
        return s == '' and seq == [] # if both ran out at the same time, the string was successfully built

    r = RULES[seq[0]] # get the definition of the first rule in the sequence
    if '"' in r: # our rule is for a primitive
        if s[0] in r: # and our first character matches that primitive
            return can_be_built(s[1:], seq[1:]) # strip off the match and keep going
        else:
            return False #the first char didn't match
    else:
        return any(can_be_built(s, t + seq[1:]) for t in r) # superimpose the new rules into place and check again

def parse_rule(s):
    n, e = s.split(": ")
    if '"' not in e:
        e = [ [int(r) for r in t.split()] for t in e.split("|")]
    return (int(n), e)
    
    



if __name__ == "__main__":
    rules_text, messages = [x.split('\n') for x in input_str.split('\n\n')]
    RULES = dict(parse_rule(r) for r in rules_text)
    print("Part 1:")
    print(sum(can_be_built(m, [0]) for m in messages))
    
    rules_text += ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]
    RULES = dict(parse_rule(r) for r in rules_text)
    print("Part 2:")
    print(sum(can_be_built(m, [0]) for m in messages))
    
    


