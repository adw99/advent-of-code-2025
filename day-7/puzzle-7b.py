import sys
import os
from typing import Tuple
import functools

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helpers')))

from grid import Grid

g = None

@functools.cache
def move_tach(tx,ty) -> int:
    global g
    total = 0
    pt = ''
    dy = ty
    while pt != '^' and dy< max_y:
        dy += 1
        pt = g.get(tx,dy)
    if dy == max_y:
        # we reached the bottom
        return 1
    else:
        total = 0
        total += move_tach(tx-1,dy)
        total += move_tach(tx+1,dy)
    return total


def solution(grid:Grid, start:Tuple[int,int]):
    # Since we're not changing the grid as we recurse I'm making it a global
    # this makes it easier to cache the move_tach function
    global g

    print(f"Start: {start}")
    g = grid
    (tx,ty) = start
    result = move_tach(tx,ty)

    return result

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 7, Part 2 ***\n")
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