import sys
from typing import List
from functools import cache

connections = {}

@cache
def recurse(pt:str, target: str) -> int:
    global connections
    result = 0
    options = connections[pt] if pt in connections else []
    for o in options:
        if o == target:
            result += 1
            # print(f"> out {result}")
        else:
            result += recurse(o,target)
    return result

def solution() -> int:
    # Assuming no cycles, then DAC witll either be 'before' or 'after FFT from the
    # POV of getting from SVR->OUT
    dtof = recurse("dac","fft")
    ftod = recurse("fft","dac")
    print(f"DAC->FFT {dtof}, FFT->DAC {ftod}")
    result = 1
    if dtof>0:
        # order is svr -> dac -> fft -> out
        result = dtof
        p1 = "dac"
        p2 = "fft"
    else:
        # order is svr -> fft -> dac -> out
        result = ftod
        p1 = "fft"
        p2 = "dac"

    result *= recurse("svr",p1)
    result *= recurse(p2,"out")

    return result

if __name__ == '__main__':    
    print(f"*** Advent of Code 2025, Day 11, Part  ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'

    df = open(fname, "r")
    boxes = []
    lines = [l.strip() for l in df.read().splitlines() if len(l.strip())>0]

    nodes = set()
    for l in lines:
        ft = l.split(':')
        f = ft[0].strip()
        t = ft[1].strip().split(' ')
        connections[f] = t
    print(f"Nodes; {len(connections.keys())}")
    result = solution()
    print(f"Result: {result}")
