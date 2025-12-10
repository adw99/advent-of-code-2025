import sys
import re
from typing import List
import itertools

def perms( target, buttons ):

    button_options = range(len(buttons))
    print(f"_perms: {target} / {buttons}")

    found = False
    clicks = 2

    while not found and clicks<99:
        # print(f"depth: {clicks}")
        options = itertools.product(button_options, repeat=clicks)
        for op in options:
            result = 0
            for num in list(op):
                result = result ^ buttons[num]
            # print(f"__{op}: {result}")
            if result == target:
                print(f"WINNER! {op}")
                return clicks
        clicks += 1                

    return clicks


def solution(machines: List[dict]) -> int:
    result = 0

    for m in machines:
        found = False
        min = 99
        for b in m['buttons']:
            if b == m['ind']:
                found = True
                min = 1
        if not found:
            min = perms(m['ind'],m['buttons'])
        print(f">> {min}")
        result += min
    return result

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 10, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'

    df = open(fname, "r")
    boxes = []
    lines = [l.strip() for l in df.read().splitlines() if len(l.strip())>0]

    rex = re.compile("\[(\W*)\] (\(.*\)) ({.*})")

    machines = []
    for l in lines:
        m = {}

        match = rex.search(l)
        ind = match.group(1)
        target =0
        # build a bitwise version of the desired state, counting from the left
        for i in range(len(ind)):
            if ind[i] == '#':
                target += 2**i
        m['ind'] = target

        # build a bitwise mask for the actions of each button

        buttons = []
        wiring = match.group(2).split(' ')
        for w in wiring:
            b = 0
            bl = [int(x) for x in w[1:-1].split(',')]
            for n in bl:
                b = b | 2**n
            buttons.append( b )
        m['buttons'] = buttons

        jreq = match.group(3)
        m['jreq'] = jreq[1:-1].split(',') # presumably for part 2
        print(f">> {m}")

        machines.append(m)
                        
    print(f"Machines: {len(machines)}")
    result = solution(machines)
    print(f"Result: {result}")