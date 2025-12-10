import sys
import re
from typing import List
from pulp import *

def find_j_in_bs(j,buttons):
    result = []
    for i in range(len(buttons)):
        if j in buttons[i]:
            result.append(i)
    return result

def solve_machine(machine: dict) -> int:

    model = LpProblem( f"AOC25", LpMinimize)
    b_list = machine['buttons']
    buttons = len(b_list)

    vars = []
    for b in range(buttons):
        vars.append( LpVariable( f"x{b}", 0, None, LpInteger))

    model += lpSum([x for x in vars]), "Total Sum of Variables"

    j_list = machine['jreq']
    jolts = len(j_list)

    for j in range(jolts):
        btns = find_j_in_bs(j,b_list)
        model += lpSum( vars[x] for x in btns ) == j_list[j]
        
    
    model.solve(PULP_CBC_CMD(msg=False))
    result = 0
    for v in vars:
        if v.name.startswith('x'):
            result += int(v.varValue)
    return result


def solution(machines: List[dict]) -> int:
    result = 0

    for m in machines:
        result += solve_machine(m)
    return result

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 10, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'

    df = open(fname, "r")
    boxes = []
    lines = [l.strip() for l in df.read().splitlines() if len(l.strip())>0]

    rex = re.compile("\[(\W*)\] (\(.*\)) ({.*})")

    machines = []
    for l in lines:
        m = {}

        match = rex.search(l)

        buttons = []
        wiring = match.group(2).split(' ')
        for w in wiring:
            buttons.append([int(x) for x in w[1:-1].split(',')])
        m['buttons'] = buttons

        jreq = match.group(3)
        m['jreq'] = [int(x) for x in jreq[1:-1].split(',')]

        machines.append(m)
                        
    print(f"Machines: {len(machines)}")
    result = solution(machines)
    print(f"Result: {result}")