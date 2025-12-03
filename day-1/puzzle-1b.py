import sys
import re
from typing import List,Tuple

debug = False

def dprint(fs,end='\r\n'):
    if debug:
        print(fs, end=end)


def solution(rot: List[Tuple[str,int]]) -> int:
    pos = 50
    zeroes = 0
    for (dir,dist) in rot:
        dprint(f"{dir}{dist}:",end='')
        if dir == 'L':
            if pos != 0 and pos-dist<0:
                zeroes += 1
                dprint('*', end='')
            if dist-pos > 100:
                # the extra -1 is to prevent double-counting a 'wraparound' that lands on zero
                dz = (dist-pos-1)//100
                dprint("^" * dz, end='')
                zeroes += dz
            pos = abs( (pos-dist) % 100)
                
        else:
            if pos + dist > 100:
                dprint('*', end='')
                zeroes += 1
            if dist-(100-pos) > 100:
                # the extra -1 is to prevent double-counting a 'wraparound' that lands on zero
                dz = (dist-(100-pos)-1)//100
                zeroes += dz
                dprint("#" * dz, end='')
            pos = (pos + dist) % 100

        if pos == 0:
            dprint(f"@", end='')
            zeroes += 1
        dprint(f" -> {pos}")

    return zeroes

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 1, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]
    rot = []
    _rex = re.compile("([LR])(\d+)")
    for l in lines:
        g = _rex.search(l)
        rot.append( (g[1],int(g[2])))
    
    print(f"Rotations: {len(rot)}")

    result = solution(rot)
    print(f"Solution: {result}")