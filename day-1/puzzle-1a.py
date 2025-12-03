import sys
import re
from typing import List,Tuple


def solution(rot: List[Tuple[str,int]]) -> int:
    pos = 50
    zeroes = 0
    for (dir,dist) in rot:
        if dir == 'L':
            pos = abs( (pos-dist) % 100)
        else:
            pos = (pos + dist) % 100
        if pos == 0:
            zeroes += 1
        print(f"{dir}{dist} -> {pos}")

    return zeroes

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 1, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]
    rot = []
    _rex = re.compile("([LR])(\d+)")
    for l in lines:
        g = _rex.search(l)
        rot.append( (g[1],int(g[2])))
    
    print(f"Rotations: \r\n{rot}")

    result = solution(rot)
    print(f"Solution: {result}")