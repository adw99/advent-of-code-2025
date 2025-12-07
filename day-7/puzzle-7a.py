import sys
import os
from typing import Tuple

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helpers')))

from grid import Grid

def solution(grid:Grid, start:Tuple[int,int]):
    print(f"Start: {start}")

    splits = 0
    tachyons = [start]
    for y in range(1,max_y+1):
        new_tach= set()
        for (tx,ty) in tachyons:
            pt = grid.get(tx,y)
            if pt == '.':
                # no split
                new_tach.add((tx,y))
            elif pt == '^':
                # split
                splits += 1
                new_tach.add( (tx-1,y))
                new_tach.add( (tx+1,y))
        tachyons = list(new_tach)

    return splits

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 7, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]

    max_x = len(lines[0])-1
    max_y = len(lines)-1
    grid = Grid(max_x=len(lines[0]), max_y=len(lines))
    start = ()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid.set(x,y,lines[y][x])
            if lines[y][x] == "S":
                start = (x,y)
    result = solution(grid,start)
    print(f"Result: {result}")